import factory


class AboutUsFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = "website.AboutUs"

    address = factory.Faker("address")
