from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class PhoneNumber(models.Model):
    phone_number_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '+999999999'."),
            _("Up to 15 digits allowed."),
        ),
    )
    phone_number = models.CharField(
        max_length=15,
        validators=[phone_number_regex],
        verbose_name=_("phone number"),
    )
    about_us = models.ForeignKey(
        "website.AboutUs",
        related_name="phone_numbers",
        on_delete=models.CASCADE,
    )

    details = models.TextField(max_length=200, verbose_name=_("details"))

    def __str__(self):
        return self.phone_number
