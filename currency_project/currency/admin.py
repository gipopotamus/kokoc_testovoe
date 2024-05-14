from django.contrib import admin
from .models import Currency, ExchangeRate


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('char_code', 'name')
    search_fields = ('char_code', 'name')


@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('currency', 'date', 'value')
    list_filter = ('date', 'currency')
    search_fields = ('currency__name', 'currency__char_code')
    date_hierarchy = 'date'
