from django.test import TestCase

from src.apps.blog.services import get_news_data
from src.apps.blog.tests.fakers import NewsFactory
from src.utils.exeptions import NotFoundException


class GetNewsDataServiceTestCase(TestCase):
    def test_news_service(self):
        with self.assertRaises(NotFoundException):
            get_news_data()
        self.news = NewsFactory()
        self.news = NewsFactory.create_batch(5)
        news, news_count = get_news_data(offset=1, limit=1)
        news_object_dict = {
            "title": self.news[0].title,
            "content": self.news[0].content,
            "slug": self.news[0].slug,
        }
        self.assertEqual(news[0], news_object_dict)
