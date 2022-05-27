from rest_framework import serializers

from src.apps.blog.models import NewsCategory
from src.apps.blog.serializers import NewsSerializer


class NewsCategorySerializer(serializers.ModelSerializer):
    news_set = NewsSerializer(many=True, read_only=True, allow_null=True)

    class Meta:
        model = NewsCategory
        fields = (
            "text",
            "news_set",
        )
