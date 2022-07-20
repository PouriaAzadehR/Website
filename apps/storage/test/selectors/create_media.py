from django.test import TestCase

from src.apps.storage.selectors import create_media, create_public_media
from src.apps.storage.tests.fakers import fake_image


class CreateMediaSelectorTestCase(TestCase):
    def setUp(self):
        self.media = fake_image(color="green")
        self.media_bytes = self.media.file.read()

    def test_create_media_selectors(self):
        media_object = create_media(media=self.media)
        media = media_object.file
        media_bytes = media.file.read()
        self.assertEqual(self.media_bytes, media_bytes)

    def test_create_public_media_selectors(self):
        media_object = create_public_media(media=self.media)
        media = media_object.file
        media_bytes = media.file.read()
        self.assertEqual(self.media_bytes, media_bytes)
