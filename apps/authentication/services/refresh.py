from src.apps.authentication.functions import refresh as refresh_function


def refresh(token):
    return refresh_function(token=token)
