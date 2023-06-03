from rest_framework.throttling import SimpleRateThrottle


class SendOneTimePasswordThrottleByDataHour(SimpleRateThrottle):
    def get_cache_key(self, request, view):
        phone_number = request.data.get("phone_number")
        if phone_number is not None:
            phone_number = "{}-throttle".format(phone_number)
        return phone_number

    scope = "otp_hour"


class SendOneTimePasswordThrottleByDataDay(
    SendOneTimePasswordThrottleByDataHour
):
    scope = "otp_day"


class SendOneTimePasswordThrottleByIPHour(SimpleRateThrottle):
    def get_cache_key(self, request, view):
        remote_addr = request.META.get("REMOTE_ADDR")
        client_ip = request.META.get("X-Forwarded-For", remote_addr)
        key = "{}-newsletter".format(client_ip)
        return key

    scope = "otp_hour"


class SendOneTimePasswordThrottleByIPDay(SendOneTimePasswordThrottleByIPHour):
    scope = "otp_day"
