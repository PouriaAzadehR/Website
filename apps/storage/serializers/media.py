from rest_framework import serializers

from src.apps.storage.models import MediaModel


class MediaModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaModel
        fields = ("file",)
