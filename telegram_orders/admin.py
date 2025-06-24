from django.contrib import admin
from .models import TelegramRequest

@admin.register(TelegramRequest)
class TelegramRequestAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'language', 'service', 'subservice', 'tariff', 'price', 'created_at')
    search_fields = ('full_name', 'phone_number', 'service')
