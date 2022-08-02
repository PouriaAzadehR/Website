import uuid

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from src.apps.authentication.models.user_manager import UserManager

REQUIRED_FIELDS_FOR_EACH_USER = {
    "ST": [
        "sharif_id",
        "faculty",
        "national_id",
        "first_name",
        "last_name",
        "gender",
    ],
    "PN": ["national_id", "first_name", "last_name", "gender"],
    "FM": [
        "sharif_id",
        "faculty",
        "national_id",
        "first_name",
        "last_name",
        "gender",
    ],
    "AD": [],
    "GR": ["national_id", "first_name", "last_name", "gender"],
    "GE": ["national_id", "first_name", "last_name", "gender"],
}


class User(AbstractUser):
    class UserType(models.TextChoices):
        STUDENT = "ST", _("Student")
        FACULTY_MEMBER = "FM", _("Faculty Member")
        PERSONNEL = "PN", _("Personnel")
        GRADUATE = "GR", _("Graduate")
        GUEST = "GE", _("Guest")
        ADMIN = "AD", _("Admin")

    username = None
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user_type = models.CharField(
        max_length=2, choices=UserType.choices, default=UserType.GUEST
    )
    phone_regex = RegexValidator(
        regex=r"^\+?1?\d{9,15}$",
        message="{}\n{}".format(
            _("Phone number must be entered in the format: '+999999999'."),
            _("Up to 15 digits allowed."),
        ),
    )
    phone_number = models.CharField(
        verbose_name=_("phone number"),
        validators=[phone_regex],
        max_length=17,
        blank=False,
        unique=True,
        null=False,
    )
    # Sharif ID will use the same fields for different entities
    # For Students it will be the Student Number
    # For Faculty Members it will their ID
    # For Personnel it will be the Personnel ID
    # For Non-Sharif Members it will be blank
    sharif_id = models.CharField(
        verbose_name=_("sharif identification number"),
        max_length=30,
        null=True,
        blank=True,
        unique=True,
    )
    national_id_regex = RegexValidator(
        regex=r"\d{10}$",
        message="{}\n{}\n{}".format(
            _("National ID should be in this format: '1111111111'."),
            _("Don't use - inside of it."),
            _("It should be exactly 10 characters long."),
        ),
    )
    national_id = models.CharField(
        verbose_name=_("national identification number"),
        validators=[national_id_regex],
        max_length=10,
        null=True,
        blank=True,
    )
    is_national_id_verified = models.BooleanField(default=False)
    national_card = models.ForeignKey(
        "storage.MediaModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="national_card",
    )
    faculty = models.ForeignKey(
        "authentication.Faculty",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_faculty",
    )
    avatar = models.ForeignKey(
        "storage.MediaModel",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="user_avatar",
    )
    birth_date = models.DateField(blank=True, null=True)
    gender_choices = (("M", _("Male")), ("F", _("Female")))
    gender = models.CharField(
        max_length=1, choices=gender_choices, blank=True, null=True
    )
    city = models.CharField(max_length=40, blank=True, null=True)
    has_accepted_terms = models.BooleanField(default=False)
    dorm = models.BooleanField(default=False)
    objects = UserManager()
    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []
    is_notifications_disabled = models.BooleanField(default=False)

    @property
    def is_profile_completed(self):
        required_fields = REQUIRED_FIELDS_FOR_EACH_USER.get(self.user_type)
        for field in required_fields:
            if getattr(self, field) is None:
                return False
        return True

    @property
    def is_sharif_member(self):
        if self.sharif_id is not None:
            return True
        else:
            return False

    @property
    def is_registered(self):
        if (
            self.birth_date is None
            or self.gender is None
            or self.city is None
            or self.first_name is None
            or self.last_name is None
        ):
            return False
        return True

    def clean(self):
        # Guest Users and admins Can't have the sharif_id Value
        sharif_id_not_required = ["GE", "AD"]
        if (
            self.user_type in sharif_id_not_required
            and self.sharif_id is not None
        ):
            raise ValidationError(
                _("This specific user type can't have a sharif_id")
            )
        sharif_id_required = ["ST", "FM", "PN"]
        if self.user_type in sharif_id_required and self.sharif_id is None:
            raise ValidationError(_("Sharif Members must provide their id"))

    def save(self, *args, **kwargs):
        if self.password is None or self.password == "":
            self.set_unusable_password()
        self.full_clean()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        if self.is_sharif_member:
            return "{}-{}-{}".format(
                self.sharif_id,
                self.get_user_type_display(),
                self.last_name,
            )
        else:
            return "{}-{}-{}".format(
                self.phone_number, self.get_user_type_display(), self.last_name
            )
