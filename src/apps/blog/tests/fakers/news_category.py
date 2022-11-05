import factory

from src.apps.blog.models import NewsCategory


class NewsCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = NewsCategory

    text = factory.sequence(lambda n: "text%d" % n)
