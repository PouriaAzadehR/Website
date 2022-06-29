from src.apps.storage.selectors import create_media as create_media_selector
from src.apps.storage.selectors import (
    create_public_media as create_public_media_selector,
)


def create_media(media):
    media_object = create_media_selector(media=media)
    return media_object.id


def create_public_media(media):
    media_object = create_public_media_selector(media=media)
    return media_object.id
