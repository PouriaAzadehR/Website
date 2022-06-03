import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Ticket(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    email = models.EmailField(verbose_name=_("email"))

    message = models.TextField(
        verbose_name=_("message"), blank=True, null=True
    )

    created_at = models.DateTimeField(
        verbose_name=_("created_at"), auto_now_add=True
    )

    class Meta:
        ordering = ("-created_at",)
