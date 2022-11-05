from src.apps.website.serializers import TicketSerializer
from src.static import SerializerErrors
from src.utils import BadRequestException


def create_ticket(data):
    serializer = TicketSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return serializer.data
    errors = serializer.errors
    error_types = []
    for error in errors.keys():
        error_type = SerializerErrors.TicketRegistrationSerializer.errors.get(
            error
        )
        error_types.append(error_type)
    raise BadRequestException(message=errors, error_type=error_types)
