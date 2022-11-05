from django.test import TestCase

from src.apps.blog.selectors import get_news_list
from src.apps.blog.tests.fakers import NewsFactory


class GetNewsListSelectorTestCase(TestCase):
    def setUp(self) -> None:
        self.assertIsNone(get_news_list())
        self.news = NewsFactory()

    def test_get_news_list_selector(self):
        news = get_news_list()
        self.assertEqual(len(news), 1)
        self.assertEqual(news[0], self.news)
