from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.blog.services import get_about_us_list


class GetAboutUsNews(APIView):
    def get(self, *args, **kwargs):
        data = get_about_us_list()
        return Response(
            data={"ok": True, "data": data, "status": status.HTTP_200_OK},
            status=status.HTTP_200_OK,
        )
