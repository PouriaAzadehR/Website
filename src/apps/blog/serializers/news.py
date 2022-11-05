from rest_framework import serializers

from src.apps.blog.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = (
            "title",
            "content",
            "slug",
        )
