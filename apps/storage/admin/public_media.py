from django.contrib import admin

from src.apps.storage.models import PublicMediaModel


@admin.register(PublicMediaModel)
class PublicMediaModelAdmin(admin.ModelAdmin):
    pass # just for registriation
