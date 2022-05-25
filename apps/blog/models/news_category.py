import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class NewsCategory(models.Model):
    id = models.UUIDField(editable=False, primary_key=True, default=uuid.uuid4)
    slug = models.SlugField(verbose_name=_("slug"), unique=True)
    text = models.CharField(max_length=100, verbose_name=_("text"))
    created_at = models.DateField(
        auto_now_add=True, verbose_name=_("created_at")
    )
    updated_at = models.DateField(auto_now=True, verbose_name=_("updated_at"))

    def __str__(self):
        return self.text
