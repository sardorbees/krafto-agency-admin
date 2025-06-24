# telegram_notify/admin.py
from django.contrib import admin
from .models import TelegramMessage

@admin.register(TelegramMessage)
class TelegramMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'message', 'sent_at')
    readonly_fields = ('sent_at',)
