import uuid

from django.db import models


class NCVerification(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        "authentication.User", on_delete=models.CASCADE, related_name="nc_user"
    )
    national_card = models.ForeignKey(
        "storage.MediaModel",
        on_delete=models.SET_NULL,
        null=True,
        related_name="nc_image",
    )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __init__(self, *args, **kwargs):
        super(NCVerification, self).__init__(*args, **kwargs)
        self.__old_is_verified = self.is_verified

    def save(self, *args, **kwargs):
        if not self.__old_is_verified and self.is_verified:
            self.user.is_national_id_verified = True
            self.user.national_card = self.national_card
            self.user.save()
        self.full_clean()
        super(NCVerification, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.id}-{self.self.is_verified}"
