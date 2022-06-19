from django.contrib import admin

from src.apps.terms.admin.terms import TermInlineAdmin
from src.apps.terms.models.terms_category import TermsCategory


@admin.register(TermsCategory)
class TermsCategoryAdmin(admin.ModelAdmin):
    inlines = [TermInlineAdmin]
