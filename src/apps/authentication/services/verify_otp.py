from src.apps.authentication.models import OneTimePassword
from src.apps.authentication.selectors import get_user_by_id
from src.utils import InvalidOTP


def verify_otp_and_get_user_id(otp_id, otp_code):
    try:
        user_id = OneTimePassword.verify_otp(otp_id=otp_id, otp_code=otp_code)
        user = get_user_by_id(user_id=user_id)
        if not user.is_active:
            user.is_active = True
            user.save()
        return user_id
    except InvalidOTP:
        return None
