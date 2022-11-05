from django.test import TestCase

from src.apps.storage.selectors import get_media_by_id, get_public_media_by_id
from src.apps.storage.tests.fakers import (
    MediaModelFactory,
    PublicMediaModelFactory,
)


class GetMediaSelectorTestCase(TestCase):
    def setUp(self):
        self.media = MediaModelFactory()
        self.public_media = PublicMediaModelFactory()

    def tests_get_media_by_id_selector(self):
        media = get_media_by_id(self.media.id)
        self.assertEqual(media, self.media)

    def tests_get_public_media_by_id_selector(self):
        media = get_public_media_by_id(self.public_media.id)
        self.assertEqual(media, self.public_media)
