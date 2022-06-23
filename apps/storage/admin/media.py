from django.contrib import admin

from src.apps.storage.models import MediaModel


@admin.register(MediaModel)
class MediaModelAdmin(admin.ModelAdmin):
    pass
