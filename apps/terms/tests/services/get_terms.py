import random

from django.test import TestCase

from src.apps.terms.serializers import TermsCategorySerializer, TermSerializer
from src.apps.terms.services import get_terms
from src.apps.terms.tests.fakers.terms import TermFactory
from src.apps.terms.tests.fakers.terms_category import TermsCategoryFactory


class GetTermsServiceTestCase(TestCase):
    def setUp(self):
        category = TermsCategoryFactory()
        term_count = random.randint(1, 10)
        self.category_data = TermsCategorySerializer(category).data
        self.terms = []
        for _ in range(term_count):
            term = TermFactory(category=category)
            data = TermSerializer(term).data
            self.terms.append(data)

    def test_get_terms_service(self):
        categories = get_terms()
        self.assertEqual(len(categories), 1)
        terms = categories[0].get("terms")
        self.assertListEqual(self.terms, list(terms))
