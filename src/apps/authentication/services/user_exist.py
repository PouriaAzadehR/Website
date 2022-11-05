from src.apps.authentication.selectors import (
    user_with_id_exists as user_with_id_exists_selector,
)


def user_with_id_exists(user_id):
    exists = user_with_id_exists_selector(user_id=user_id)
    return exists
