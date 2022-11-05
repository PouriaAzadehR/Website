from rest_framework import serializers

from src.apps.blog.models import News
from src.apps.storage.services import serialize_media_by_id


class ImportantNewsSerializer(serializers.ModelSerializer):
    preview_image = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = News
        fields = (
            "title",
            "preview_image",
            "slug",
        )

    def get_preview_image(self, obj):
        if obj.preview_image is None:
            return None
        return serialize_media_by_id(media_id=obj.preview_image.id) 
    
