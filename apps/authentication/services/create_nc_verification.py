from django.db import transaction

from src.apps.authentication.selectors import (
    create_nc_verification as create_nc_verification_selector,
)


@transaction.atomic
def create_nc_verification(user_id, media_id):
    done = False
    nc_verification_id = None
    err = None
    try:
        nc_verification = create_nc_verification_selector(
            user_id=user_id, media_id=media_id
        )
        done = True
        nc_verification_id = nc_verification.id
    except Exception as e:
        err = str(e)
    return done, nc_verification_id, err
