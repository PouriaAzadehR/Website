import uuid
from typing import Union

from src.apps.storage.models import MediaModel, PublicMediaModel


def get_media_by_id(media_id: Union[str, uuid.UUID]):
    media = MediaModel.objects.get(id=media_id)
    return media


def get_public_media_by_id(media_id: Union[str, uuid.UUID]):
    media = PublicMediaModel.objects.get(id=media_id)
    return media
