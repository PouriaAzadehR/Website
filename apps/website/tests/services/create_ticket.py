import factory
from django.test import TestCase

from src.apps.website.services import create_ticket
from src.apps.website.tests.fakers import TicketFactory
from src.utils import BadRequestException


class CreateTicketServiceTestCase(TestCase):
    def setUp(self):
        self.ticket = TicketFactory()

    def test_create_ticket_service(self):
        invalid_data = {
            "email": "invalid",
            "message": "invalid",
        }
        with self.assertRaises(BadRequestException):
            create_ticket(data=invalid_data)
        valid_data = {
            "email": factory.Faker("email"),
            "message": "valid",
        }
        ticket_info = create_ticket(data=valid_data)
        self.assertDictEqual(ticket_info, valid_data)
