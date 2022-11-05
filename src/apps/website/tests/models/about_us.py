from django.core.exceptions import ValidationError
from django.test import TestCase

from src.apps.website.models.about_us import AboutUs
from src.apps.website.tests.fakers import AboutUsFactory


class AboutUsModelTestCase(TestCase):
    def setUp(self):
        self.about_us = AboutUsFactory()

    def test_about_us_save_method(self):
        with self.assertRaises(ValidationError):
            AboutUsFactory()
        about_us = AboutUs.objects.all().first()
        about_us.address = "update"
        about_us.save()
        about_us = AboutUs.objects.all().first()

        self.assertEqual(about_us.address, "update")
