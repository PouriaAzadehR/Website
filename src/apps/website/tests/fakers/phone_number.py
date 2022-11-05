import factory

from src.apps.website.tests.fakers import AboutUsFactory


class PhoneNumberFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "website.PhoneNumber"

    phone_number = factory.Faker("numerify", text="###########")
    about_us = factory.SubFactory(AboutUsFactory)
