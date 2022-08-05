from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _

from src.apps.authentication.admin.forms import (
    UserChangeForm,
    UserCreationForm,
)
from src.apps.authentication.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "phone_number",
                    "user_type",
                )
            },
        ),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "gender",
                    "birth_date",
                    "national_id",
                    "sharif_id",
                    "avatar",
                    "dorm",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "is_registered",
                    "is_profile_completed",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "phone_number",
                    "user_type",
                    "first_name",
                    "last_name",
                    "gender",
                    "birth_date",
                    "national_id",
                    "sharif_id",
                    "avatar",
                ),
            },
        ),
    )
    list_display = (
        "phone_number",
        "user_type",
        "sharif_id",
        "national_id",
        "first_name",
        "last_name",
        "is_staff",
        "is_registered",
        "is_profile_completed",
        "dorm",
    )
    list_filter = ("gender", "user_type", "is_staff")
    readonly_fields = (
        "last_login",
        "date_joined",
        "is_profile_completed",
        "is_registered",
        "is_notifications_disabled",
    )
    search_fields = (
        "phone_number",
        "national_id",
        "sharif_id",
        "first_name",
        "last_name",
    )
    ordering = ("phone_number",)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields["is_staff"].disabled = True
            form.base_fields["is_superuser"].disabled = True
            form.base_fields["user_permissions"].disabled = True
        return form
