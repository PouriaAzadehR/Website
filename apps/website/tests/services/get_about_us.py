from django.test import TestCase

from src.apps.website.serializers import GetAboutUsSerializer
from src.apps.website.services import get_about_us
from src.apps.website.tests.fakers.about_us import AboutUsFactory
from src.utils import NotFoundException


class GetAboutUsServiceTestCase(TestCase):
    def test_get_about_us_service(self):
        with self.assertRaises(NotFoundException):
            get_about_us()

        self.about_us = AboutUsFactory()
        data = get_about_us()
        expeted_data = GetAboutUsSerializer(self.about_us).data
        self.assertDictEqual(expeted_data, data)
