from django.urls import path
from .views import ApplicationFormCreateAPIView
from .views import send_telegram_message

urlpatterns = [
    path('api/application/', ApplicationFormCreateAPIView.as_view(), name='application-create'),
    path('send-telegram/', send_telegram_message),
]
