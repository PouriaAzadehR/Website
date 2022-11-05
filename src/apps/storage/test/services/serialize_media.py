from django.test import TestCase

from src.apps.storage.serializers import MediaModelSerializer
from src.apps.storage.services import serialize_media_by_id
from src.apps.storage.tests.fakers import MediaModelFactory


class SerializeMediaServiceTestCase(TestCase):
    def setUp(self):
        self.media = MediaModelFactory()

    def test_serialize_media_by_id_selector(self):
        serialized_by_service = serialize_media_by_id(self.media.id)
        serialized_by_serializer = MediaModelSerializer(self.media).data
        self.assertDictEqual(serialized_by_serializer, serialized_by_service)
