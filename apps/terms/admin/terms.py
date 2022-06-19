from django.contrib import admin

from src.apps.terms.models.terms import Term


class TermInlineAdmin(admin.TabularInline):
    model = Term
    extra = 1
