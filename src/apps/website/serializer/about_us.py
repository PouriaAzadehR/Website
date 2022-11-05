from rest_framework import serializers

from src.apps.website.models import AboutUs
from src.apps.website.serializers.phone_number import GetPhoneNumberSerializer


class GetAboutUsSerializer(serializers.ModelSerializer):
    phone_numbers = GetPhoneNumberSerializer(many=True)

    class Meta:
        model = AboutUs
        fields = [
            "address",
            "longitude",
            "latitude",
            "phone_numbers",
        ]
