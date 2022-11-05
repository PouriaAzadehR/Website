from django.test import TestCase

from src.apps.blog.selectors import get_news_by_slug
from src.apps.blog.tests.fakers import NewsFactory


class GetNewsBySlugSeletorTestCase(TestCase):
    def test_get_news_by_slug_selector(self):
        self.assertIsNone(get_news_by_slug(slug="invalid"))
        self.news = NewsFactory()
        news = get_news_by_slug(slug=self.news.slug)
        self.assertEqual(news, self.news)
