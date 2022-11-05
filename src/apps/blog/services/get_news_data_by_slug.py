from src.apps.blog.selectors import get_news_by_slug
from src.apps.blog.serializers import FullNewsSerializer
from src.static import ErrorEnum
from src.utils import NotFoundException


def get_news_data_by_slug(slug):
    news_object = get_news_by_slug(slug=slug)
    if news_object is None:
        raise NotFoundException(
            message={"news": "news does not exist"},
            error_type=[ErrorEnum.Service.NEWS_DOES_NOT_EXIST],
        )
    news_serializer = FullNewsSerializer(news_object)
    return news_serializer.data
