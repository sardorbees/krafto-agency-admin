# telegram_notify/serializers.py
from rest_framework import serializers
from .models import TelegramMessage

class TelegramMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramMessage
        fields = ['id', 'message', 'sent_at']
