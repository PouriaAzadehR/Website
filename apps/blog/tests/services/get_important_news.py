from django.test import TestCase

from src.apps.blog.serializers import ImportantNewsSerializer
from src.apps.blog.services import get_important_news_list
from src.apps.blog.tests.fakers import NewsFactory
from src.utils import NotFoundException


class GetImportantNewsServiceTestCase(TestCase):
    def setUp(self):
        self.news = NewsFactory.create_batch(5, is_important=False)

    def test_get_important_news_service(self):
        with self.assertRaises(NotFoundException):
            get_important_news_list()
        featured_news = NewsFactory.create_batch(5, is_important=True)
        featured_news_data = ImportantNewsSerializer(
            featured_news, many=True
        ).data
        expected_featured_news = get_important_news_list()
        self.assertEqual(
            len(featured_news_data), len(expected_featured_news)
        )
