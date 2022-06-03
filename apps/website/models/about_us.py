import uuid

from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _


class AboutUs(models.Model):
    address = models.TextField(max_length=2000, verbose_name=_("address"))
    longitude = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        verbose_name=_("longitude"),
        null=True,
        blank=True,
    )
    latitude = models.DecimalField(
        max_digits=18,
        decimal_places=15,
        verbose_name=_("latitude"),
        null=True,
        blank=True,
    )

    def save(self, *args, **kwargs):
        if not self.pk and AboutUs.objects.exists():
            # if you'll not check for self.pk
            # then error will also raised in update of exists model

            raise ValidationError(
                _("There  can be only one About us instansce")
            )
        return super(AboutUs, self).save(*args, **kwargs)
