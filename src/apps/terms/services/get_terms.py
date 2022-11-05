from src.apps.terms.selectors import get_all_categories
from src.apps.terms.serializers import TermsCategorySerializer


def get_terms():
    terms_category = get_all_categories()
    serializer = TermsCategorySerializer(terms_category, many=True)
    serializer_data = serializer.data
    return serializer_data
