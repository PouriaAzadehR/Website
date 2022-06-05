from rest_framework import serializers

from src.apps.website.models import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = [
            "email",
            "message",
        ]
