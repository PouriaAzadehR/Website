import json
import uuid

from django.contrib.auth.hashers import check_password, make_password
from django.core.cache import cache

from settings import OTP_TTL, UNDER_DEVELOPMENT
from src.utils import InvalidOTP, generate_otp


class OneTimePassword:
    code = None
    otp_id = None
    user = None

    def __init__(self, user):
        self.otp_id = str(uuid.uuid4())
        self.user = user
        self.code = generate_otp()
        if UNDER_DEVELOPMENT:
            self.code = "123456"
        self.__save()

    def __save(self):
        cache.set(self.otp_id, self.__gen_value(), timeout=OTP_TTL)
        cache.set(self.user.phone_number, "", timeout=OTP_TTL)

    def __gen_value(self):
        raw_code = "{}{}".format(self.otp_id, self.code)
        raw_data = {
            "user_phone": self.user.phone_number,
            "user_id": str(self.user.id),
            "hash": make_password(raw_code),
        }
        return json.dumps(raw_data)

    def verify_otp(otp_id, otp_code):
        if cache.ttl(otp_id) == 0:
            raise InvalidOTP("otp is inavlid")
        value = cache.get(otp_id)
        data = json.loads(value)
        if not check_password(
            "{}{}".format(otp_id, otp_code), data.get("hash")
        ):
            raise InvalidOTP("otp is inavlid")
        return data.get("user_id")

    def otp_exist(phone_number):
        return cache.ttl(phone_number) != 0
