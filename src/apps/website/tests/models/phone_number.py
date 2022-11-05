from django.test import TestCase

from src.apps.website.tests.fakers import PhoneNumberFactory


class PhoneNumberModelTestCase(TestCase):
    def setUp(self):
        self.phone_number = PhoneNumberFactory()

    def test_phone_number_str_method(self):
        phone_number_string_object = str(self.phone_number)
        expected_string = "{}".format(self.phone_number.phone_number)
        self.assertEqual(phone_number_string_object, expected_string)
