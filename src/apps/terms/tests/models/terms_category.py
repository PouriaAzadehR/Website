from django.test import TestCase

from src.apps.terms.tests.fakers import TermsCategoryFactory


class TermsCategoryTestCase(TestCase):
    def setUp(self):
        self.category = TermsCategoryFactory()

    def test_str_method(self):
        string_term_object = str(self.category)
        self.assertEqual(string_term_object, self.category.title)
