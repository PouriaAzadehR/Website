from django.test import TestCase

from src.apps.blog.serializers import NewsSerializer
from src.apps.blog.services import get_news_data_by_slug
from src.apps.blog.tests.fakers import NewsFactory
from src.utils import NotFoundException


class GetNewsDataBySlugServiceTestCase(TestCase):
    def setUp(self):
        self.news = NewsFactory()
        self.news_data = NewsSerializer(self.news).data

    def test_get_news_by_slug_service(self):
        with self.assertRaises(NotFoundException):
            get_news_data_by_slug(slug="invalid")
        news_object = get_news_data_by_slug(slug=self.news.slug)
        self.assertDictEqual(news_object, self.news_data)
