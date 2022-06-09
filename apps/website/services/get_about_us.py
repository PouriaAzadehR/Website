from src.apps.website.selectors import get_about_us as get_about_us_selector
from src.apps.website.serializers import GetAboutUsSerializer
from src.static import ErrorEnum
from src.utils import NotFoundException


def get_about_us():
    about_us = get_about_us_selector()
    if about_us is None:
        raise NotFoundException(
            message={"about_us": "about_us does not exist"},
            error_type=[ErrorEnum.Service.ABOUT_US_DOES_NOT_EXIST],
        )
    about_us_serializer = GetAboutUsSerializer(about_us)
    return about_us_serializer.data
