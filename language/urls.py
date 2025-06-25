from django.urls import path
from .views import SetLanguageAPIView

urlpatterns = [
    path('api/set-language/', SetLanguageAPIView.as_view(), name='set-language'),
]
