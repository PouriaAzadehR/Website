import factory

from src.apps.storage.models import MediaModel


class MediaModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MediaModel

    file = factory.django.FileField()
