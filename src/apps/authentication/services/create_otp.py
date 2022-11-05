from settings import UNDER_DEVELOPMENT
from src.apps.authentication.models import OneTimePassword
from src.apps.authentication.selectors import get_user_by_id
from src.utils import send_sms_otp


def create_one_time_password(user_id):
    user = get_user_by_id(user_id=user_id)
    otp = OneTimePassword(user=user)
    if not UNDER_DEVELOPMENT:
        send_sms_otp(phone=user.phone_number, otp=otp.code)
    return otp.otp_id
