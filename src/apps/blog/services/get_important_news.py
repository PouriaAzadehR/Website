from src.apps.blog.selectors import (
    get_important_news_list as get_important_news_list_selector,
)
from src.apps.blog.serializers import ImportantNewsSerializer
from src.static import ErrorEnum
from src.utils import NotFoundException


def get_important_news_list():
    important_news = get_important_news_list_selector()
    if important_news:
        important_serializer = ImportantNewsSerializer(important_news, many=True)
    else:
        raise NotFoundException(
            message={"error": "no important news found."},
            error_type=[ErrorEnum.News.IMPORTANT_NEWS_DOES_NOT_EXIST],
        )
    return important_serializer.data
