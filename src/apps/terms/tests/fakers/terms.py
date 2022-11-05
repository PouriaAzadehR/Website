import factory

from src.apps.terms.models import Term
from src.apps.terms.tests.fakers.terms_category import TermsCategoryFactory


class TermFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Term

    title = factory.Sequence(lambda n: "term-%d" % n)
    text = factory.Sequence(lambda n: "term-%d data" % n)
    ordering = factory.Sequence(lambda n: n)
    category = factory.SubFactory(TermsCategoryFactory)
