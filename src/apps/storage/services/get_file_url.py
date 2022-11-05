from src.apps.storage.selectors import get_public_media_by_id


def get_public_file_url_by_id(media_id):
    media = get_public_media_by_id(media_id=media_id)
    url = media.file.url
    return url
