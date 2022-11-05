from src.apps.blog.models import News


def get_news_list():
    news_object = News.objects.all()
    if len(news_object) != 0:
        return news_object
    return None
