from django.utils.translation import gettext_lazy as _

from src.apps.blog.selectors import get_news_list
from src.apps.blog.serializers import NewsSerializer
from src.static import ErrorEnum
from src.utils import NotFoundException


def get_news_data(limit=None, offset=None):
    if limit is None:
        limit = 10
    if offset is None:
        offset = 0
    list_news = get_news_list()
    if list_news is None:
        raise NotFoundException(
            message={"news": _("there is no news")},
            error_type=[ErrorEnum.News.DOES_NOT_EXIST],
        )
    news_count = len(list_news)
    end = offset + limit
    list_news = list_news[offset:end]
    ser_news = NewsSerializer(list_news, many=True)
    return ser_news.data, news_count
