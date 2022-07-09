import factory

from src.apps.storage.models import PublicMediaModel


class PublicMediaModelFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PublicMediaModel

    file = factory.django.FileField()
