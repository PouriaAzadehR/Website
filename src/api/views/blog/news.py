from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.blog.services import get_news_data
from src.static import ErrorEnum
from src.utils.exeptions import BadRequestException


class GetNewsList(APIView):
    def get(self, *args, **kwargs):
        limit = self.request.query_params.get("limit", "10")
        offset = self.request.query_params.get("offset", "0")
        try:
            limit = int(limit)
            offset = int(offset)
        except Exception:
            raise BadRequestException(
                message={"news": _("limit and offset is not valid")},
                error_type=[ErrorEnum.News.INVALID_LIMIT_AND_OFFSET],
            )
        news_data, news_count = get_news_data(limit=limit, offset=offset)
        return Response(
            data={
                "ok": True,
                "data": news_data,
                "status": status.HTTP_200_OK,
                "news_count": news_count,
            },
            status=status.HTTP_200_OK,
        )
