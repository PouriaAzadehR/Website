from django.db import transaction
from django.utils import timezone

from src.apps.authentication.selectors import (
    create_guest as create_guest_selector,
)


@transaction.atomic
def create_guest(phone_number, **kwargs):
    done = False
    user_id = None
    err = None
    try:
        user = create_guest_selector(phone_number=phone_number, **kwargs)
        done = True
        user_id = user.id
    except Exception as e:
        err = str(e)
    return done, user_id, err
