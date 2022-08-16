import uuid
from typing import Union

from django.db import transaction

from src.apps.authentication.selectors import get_user_by_id
from src.apps.authentication.serializers import UpdateUserSerializer
from src.static import SerializerErrors


@transaction.atomic
def update_user_by_id(user_id: Union[str, uuid.UUID], data: dict):
    user = get_user_by_id(user_id)
    serializer = UpdateUserSerializer(instance=user, data=data, partial=True)
    errors = []
    if serializer.is_valid():
        serializer.save()
        return True, errors, None
    for field_name in serializer.errors.keys():
        errors.append(SerializerErrors.UpdateUserSerializer.errors[field_name])
    return False, errors, serializer.errors
