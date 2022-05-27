from rest_framework import serializers

from src.apps.blog.models import News
from src.apps.storage.serializers import MediaModelSerializer


class FullNewsSerializer(serializers.ModelSerializer):
    preview_image = MediaModelSerializer(read_only=True)
    category = serializers.ReadOnlyField(source='category.slug')

    class Meta:
        model = News
        fields = (
            "title",
            "content",
            "slug",
            "preview_image",
            "content",
            "created_at",
            "valid_until",
            "updated_at",
            "is_important",
            "link",
            "category",
        )
