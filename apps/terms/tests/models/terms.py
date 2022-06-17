from django.test import TestCase

from src.apps.terms.tests.fakers import TermFactory


class TermTestCase(TestCase):
    def setUp(self):
        self.term = TermFactory()

    def test_str_method(self):
        string_term_object = str(self.term)
        self.assertEqual(string_term_object, self.term.title)
