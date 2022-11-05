import factory

from src.apps.terms.models import TermsCategory


class TermsCategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = TermsCategory

    title = factory.Sequence(lambda n: "term-category-%d" % n)
    ordering = factory.Sequence(lambda n: n)
