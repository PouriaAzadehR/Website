from src.apps.blog.models import News


def get_important_news_list():
    return News.objects.filter(is_important=True)
