from src.apps.authentication.functions import login
from src.apps.authentication.models import User
from src.apps.authentication.selectors import get_user_by_id


def login_user_by_id(user_id):
    try:
        user = get_user_by_id(user_id=user_id)
    except User.DoesNotExist:
        return None
    return login(user=user)
