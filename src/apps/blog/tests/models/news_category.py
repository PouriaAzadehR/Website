from django.test import TestCase

from src.apps.blog.tests.fakers import NewsCategoryFactory


class NewsCategoryModelTestCase(TestCase):
    def setUp(self):
        self.news_category = NewsCategoryFactory()

    def test_str_method(self):
        string_news_category_object = str(self.news_category)
        self.assertEqual(string_news_category_object, self.news_category.text)
