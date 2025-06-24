# telegram_notify/views.py
from rest_framework import viewsets
from .models import TelegramMessage
from .serializers import TelegramMessageSerializer

class TelegramMessageViewSet(viewsets.ModelViewSet):
    queryset = TelegramMessage.objects.all().order_by('-sent_at')
    serializer_class = TelegramMessageSerializer
