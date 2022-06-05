from rest_framework import serializers

from src.apps.website.models import PhoneNumber


class GetPhoneNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneNumber
        fields = [
            "phone_number",
        ]
