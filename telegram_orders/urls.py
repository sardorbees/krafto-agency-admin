from django.urls import path
from .views import TelegramBotRequestView
from .views import TelegramUserCreateOrUpdateView

urlpatterns = [
    path('telegram/request/', TelegramBotRequestView.as_view(), name='telegram-request'),
    path('api/telegram/user/', TelegramUserCreateOrUpdateView.as_view(), name='telegram_user'),
]
