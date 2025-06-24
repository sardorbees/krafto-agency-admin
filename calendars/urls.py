from django.urls import path
from .views import CalendarEventAPIView

urlpatterns = [
    path('api/calendar/', CalendarEventAPIView.as_view(), name='calendar-list'),
]
