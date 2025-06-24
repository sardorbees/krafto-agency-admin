# telegram_notify/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TelegramMessageViewSet

router = DefaultRouter()
router.register('', TelegramMessageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
