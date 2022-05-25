import datetime
import uuid

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from tinymce.models import HTMLField as TinyHTMLField



def time():
    return timezone.now() + datetime.timedelta(days=30)


class News(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    title = models.CharField(max_length=60, verbose_name=_("title"))

    slug = models.SlugField(verbose_name=_("slug"), unique=True)

    preview_image = models.OneToOneField(
        "storage.MediaModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="preview_news_image",
    )

    content = TinyHTMLField(verbose_name=_("content"))

    created_at = models.DateTimeField(
        verbose_name=_("created_at"), auto_now_add=True
    )
    valid_until = models.DateField(
        verbose_name=_("valid_until"),
        default=time,
    )
    updated_at = models.DateField(verbose_name=_("updated_at"), auto_now=True)
    is_important = models.BooleanField(
        verbose_name=_("important"), default=False
    )

    link = models.URLField(verbose_name=_("link"), null=True, blank=True)

    category = models.ForeignKey(
        "blog.NewsCategory",
        on_delete=models.CASCADE,
        related_name="news_category",
        null=True,
        blank=True,
    )



    def __str__(self):
        return self.title
