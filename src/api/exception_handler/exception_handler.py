import sys
import traceback

from django.utils.translation import gettext as _
from rest_framework import status
from rest_framework.exceptions import (
    MethodNotAllowed,
    NotAuthenticated,
    PermissionDenied,
    Throttled,
)
from rest_framework.response import Response

from src.static import ErrorEnum
from src.utils import BadRequestException, NotFoundException, Unauthorized


def api_exception_handler(exc, context):
    if isinstance(exc, BadRequestException):
        return Response(
            data={
                "ok": False,
                "data": exc.message,
                "status": status.HTTP_400_BAD_REQUEST,
                "error_type": exc.error_type,
            },
            status=status.HTTP_400_BAD_REQUEST,
        )
    if isinstance(exc, NotFoundException):
        return Response(
            data={
                "ok": False,
                "data": exc.message,
                "status": status.HTTP_404_NOT_FOUND,
                "error_type": exc.error_type,
            },
            status=status.HTTP_404_NOT_FOUND,
        )
    if isinstance(exc, Unauthorized):
        return Response(
            data={
                "ok": False,
                "data": {"message": exc.message},
                "status": status.HTTP_401_UNAUTHORIZED,
                "error_type": [ErrorEnum.Authentication.UNAUTHORIZED],
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )
    if isinstance(exc, NotAuthenticated):
        return Response(
            data={
                "ok": False,
                "data": {"message": str(exc)},
                "status": status.HTTP_401_UNAUTHORIZED,
                "error_type": [ErrorEnum.Authentication.UNAUTHORIZED],
            },
            status=status.HTTP_401_UNAUTHORIZED,
        )
    if isinstance(exc, PermissionDenied):
        return Response(
            data={
                "ok": False,
                "data": {"message": _("user does not have permission.")},
                "status": status.HTTP_403_FORBIDDEN,
                "error_type": [ErrorEnum.Authentication.FORBIDDEN],
            },
            status=status.HTTP_403_FORBIDDEN,
        )
    if isinstance(exc, Throttled):
        return Response(
            data={
                "ok": False,
                "data": {"message": str(exc)},
                "status": status.HTTP_429_TOO_MANY_REQUESTS,
                "error_type": [ErrorEnum.HTTP.THROTTLED],
            },
            status=status.HTTP_429_TOO_MANY_REQUESTS,
        )
    if isinstance(exc, MethodNotAllowed):
        return Response(
            data={
                "ok": False,
                "data": {"message": str(exc)},
                "status": status.HTTP_405_METHOD_NOT_ALLOWED,
                "error_type": [ErrorEnum.HTTP.METHOD_NOT_ALLOWED],
            },
            status=status.HTTP_405_METHOD_NOT_ALLOWED,
        )
    print(type(exc), exc.args, exc, end="\n")
    traceback.print_exception(*sys.exc_info())
    return Response(
        data={
            "ok": False,
            "data": {"message": str(exc)},
            "status": status.HTTP_500_INTERNAL_SERVER_ERROR,
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )
