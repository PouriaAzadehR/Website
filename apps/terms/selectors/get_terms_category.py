from src.apps.terms.models.terms_category import TermsCategory


def get_all_categories():
    terms_categories = TermsCategory.objects.all()
    return terms_categories
