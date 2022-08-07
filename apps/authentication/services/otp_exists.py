from src.apps.authentication.models import OneTimePassword


def one_time_password_exists(phone_number):
    return OneTimePassword.otp_exist(phone_number=phone_number)
