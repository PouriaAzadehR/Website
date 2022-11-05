from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from src.apps.blog.services import search_news
from src.static import ErrorEnum
from src.utils import BadRequestException


class SearchNews(APIView):
    permission_classes = []

    def get(self, *args, **kwargs):

        query = dict(self.request.query_params)
        data = {}

        single_key = "page"
        list_key = "category_slug"
        key = "search_string"
        if single_key in query.keys():
            data[single_key] = query.get(single_key)

        if list_key in query.keys():
            data[list_key] = "|".join(query.get(list_key))

        if key in query.keys():
            data[key] = "+".join(query.get(key))

        try:
            search_result, total_results = search_news(**data)

        except Exception:
            raise BadRequestException(
                message={"query_params": _("invalid query parameters")},
                error_type=[ErrorEnum.SearchPosts.INVALID_QUERY],
            )

        return Response(
            data={
                "ok": True,
                "data": {
                    "search_result": search_result,
                    "total_results": total_results,
                },
                "status": status.HTTP_200_OK,
            }
        )
