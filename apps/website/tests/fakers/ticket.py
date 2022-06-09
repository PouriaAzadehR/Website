import factory

from src.apps.website.models import Ticket


class TicketFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ticket

    email = factory.Faker("email")
    message = factory.Faker("text")
