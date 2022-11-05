from src.apps.authentication.functions import (
    validate_token as validate_token_function,
)


def validate_token(token):
    return validate_token_function(token)
