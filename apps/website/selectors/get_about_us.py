from src.apps.website.models import AboutUs


def get_about_us():
    about_us = AboutUs.objects.all().first()
    return about_us
