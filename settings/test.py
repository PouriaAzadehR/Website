from os.path import join

from settings.common import *

########## TEST SETTINGS
TEST_DISCOVER_TOP_LEVEL = PACKAGE_ROOT
TEST_DISCOVER_ROOT = join(PACKAGE_ROOT, "tests")
TEST_DISCOVER_PATTERN = "test_*.py"


########## RESTFARMEWORK CONFIGURATION
REST_FRAMEWORK = {
    "DEFAULT_THROTTLE_RATES": {
        "otp_hour": "1000/hour",
        "otp_day": "1000/day",
    },
    "EXCEPTION_HANDLER": "src.api.exception_handler.api_exception_handler",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "src.apps.authentication.backends.JWTAuthentication",
    ),
}
########## END RESTFARMEWORK CONFIGURATION
