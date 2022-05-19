from os import environ

stage = environ.get("STAGE")
if not stage:
    raise ValueError("stage is not set")

if stage == "production":
    from settings.production import *
elif stage == "ci":
    from settings.test import *
else:
    from settings.dev import *
