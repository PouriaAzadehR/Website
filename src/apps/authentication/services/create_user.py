from django.db import transaction
from django.utils import timezone

from src.apps.authentication.selectors import (
    create_user as selectors_create_user,
)


@transaction.atomic
def create_user(phone_number, full_name=None, **kwargs):
    done = False
    user_id = None
    err = None
    try:
        user = selectors_create_user(
            phone_number=phone_number,
            full_name=full_name,
            accept_terms_date=timezone.now(),
            **kwargs
        )
        done = True
        user_id = user.id
    except Exception as e:
        err = str(e)
    return done, user_id, err
