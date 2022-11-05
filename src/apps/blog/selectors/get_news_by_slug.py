from src.apps.blog.models import News


def get_news_by_slug(slug: str):
    try:
        news_object = News.objects.get(slug=slug)
    except News.DoesNotExist:
        return None
    return news_object
