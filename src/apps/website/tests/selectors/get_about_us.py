from django.test import TestCase

from src.apps.website.selectors import get_about_us
from src.apps.website.tests.fakers import AboutUsFactory


class GetAboutUsSelectorTestCase(TestCase):
    def setUp(self):
        self.about_us = AboutUsFactory()

    def test_get_about_us_selector(self):
        about_us = get_about_us()
        self.assertEqual(about_us, self.about_us)
