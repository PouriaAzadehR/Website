from src.apps.authentication.models import User
from src.apps.authentication.selectors import (
    get_user_by_id,
    get_user_by_phone_number,
)
from src.apps.authentication.serializers import GetUserDataSerializer
from src.utils import InvalidPhoneNumber, InvalidUserID


def get_user_id_by_phone_number(phone_number):
    try:
        user = get_user_by_phone_number(phone_number=phone_number)
    except User.DoesNotExist:
        raise InvalidPhoneNumber()
    return user.id


def get_user_data_by_id(user_id):
    try:
        user = get_user_by_id(user_id=user_id)
    except User.DoesNotExist:
        raise InvalidUserID()
    serializer = GetUserDataSerializer(instance=user)
    serializer_data = serializer.data
    return serializer_data
