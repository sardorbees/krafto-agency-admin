# orders/urls.py

from django.urls import path
from .views import OrderCreateView

urlpatterns = [
    path('create/', OrderCreateView.as_view(), name='create-order'),
]
