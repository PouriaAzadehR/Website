import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TermsCategory(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=64, verbose_name=_("title"))
    ordering = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("terms category")
        verbose_name_plural = _("terms categories")
        ordering = ("ordering",)
