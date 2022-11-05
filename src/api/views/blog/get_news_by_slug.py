from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.blog.services import get_news_data_by_slug


class GetNewsBySlug(APIView):
    def get(self, *args, **kwargs):
        slug = kwargs.get("slug")
        data = get_news_data_by_slug(slug=slug)
        return Response(
            data={"ok": True, "data": data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )
