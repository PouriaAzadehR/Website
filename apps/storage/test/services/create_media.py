from django.test import TestCase

from src.apps.storage.models import MediaModel, PublicMediaModel
from src.apps.storage.services import create_media, create_public_media
from src.apps.storage.tests.fakers import fake_image


class CreateMediaServiceTestCase(TestCase):
    def setUp(self):
        self.media = fake_image(color="blue")
        self.media_bytes = self.media.file.read()

    def test_create_media_service(self):
        media_id = create_media(media=self.media)
        media_object = MediaModel.objects.get(id=media_id)
        media = media_object.file
        media_bytes = media.file.read()
        self.assertEqual(self.media_bytes, media_bytes)

    def test_create_public_media_service(self):
        media_id = create_public_media(media=self.media)
        media_object = PublicMediaModel.objects.get(id=media_id)
        media = media_object.file
        media_bytes = media.file.read()
        self.assertEqual(self.media_bytes, media_bytes)
