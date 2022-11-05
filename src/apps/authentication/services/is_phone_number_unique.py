from src.apps.authentication.selectors import user_with_phone_exists


def phone_number_is_unique(phone_number):
    return not user_with_phone_exists(phone_number=phone_number)
