import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _
from tinymce import models as tinymce

from src.apps.terms.models.terms_category import TermsCategory


class Term(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=64, verbose_name=_("title"))
    text = tinymce.HTMLField(verbose_name=_("text"))
    ordering = models.IntegerField()
    category = models.ForeignKey(
        TermsCategory,
        on_delete=models.CASCADE,
        related_name="terms",
        verbose_name=_("category"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("term")
        verbose_name_plural = _("terms")
        ordering = ("ordering",)
