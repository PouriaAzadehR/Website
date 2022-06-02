from django.test import TestCase

from src.apps.blog.tests.fakers import NewsFactory


class NewsModelTestCase(TestCase):
    def setUp(self):
        self.news = NewsFactory()

    def test_str_method(self):
        string_news_object = str(self.news)
        self.assertEqual(string_news_object, self.news.title)
