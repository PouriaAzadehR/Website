import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class MediaType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=True)
    media_type = models.CharField(max_length=100, verbose_name=_("media type"))

    def __str__(self):
        return self.media_type
