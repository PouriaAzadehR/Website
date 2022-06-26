from django.db import transaction

from src.apps.storage.models import MediaModel, PublicMediaModel


@transaction.atomic
def create_media(media):
    media_object = MediaModel.objects.create(file=media)
    return media_object


@transaction.atomic
def create_public_media(media):
    media_object = PublicMediaModel.objects.create(file=media)
    return media_object
