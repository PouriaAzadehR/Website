from django.contrib import admin

from src.apps.authentication.models import NCVerification


@admin.register(NCVerification)
class NCVerificationAdmin(admin.ModelAdmin):
    pass
