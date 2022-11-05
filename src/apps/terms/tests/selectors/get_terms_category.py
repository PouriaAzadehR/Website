import random

from django.test import TestCase

from src.apps.terms.selectors import get_all_categories
from src.apps.terms.tests.fakers.terms_category import TermsCategoryFactory


class GetCategorySelectorTestCase(TestCase):
    def setUp(self):
        category_count = random.randint(1, 10)
        self.categories = []
        for _ in range(category_count):
            self.categories.append(TermsCategoryFactory())

    def test_get_all_categories_selector(self):
        categories = get_all_categories()
        self.assertListEqual(self.categories, list(categories))
