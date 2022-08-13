from src.apps.authentication.selectors import get_user_by_id


def user_is_active(user_id):
    user = get_user_by_id(user_id=user_id)
    return user.is_active
