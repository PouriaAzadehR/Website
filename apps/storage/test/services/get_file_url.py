from django.test import TestCase

from src.apps.storage.services import get_public_file_url_by_id
from src.apps.storage.tests.fakers import PublicMediaModelFactory


class GetFileUrlServiceTestCase(TestCase):
    def setUp(self):
        self.media = PublicMediaModelFactory()

    def test_get_public_file_url_by_id_service(self):
        file_url = get_public_file_url_by_id(self.media.id)
        self.assertEqual(file_url, self.media.file.url)
