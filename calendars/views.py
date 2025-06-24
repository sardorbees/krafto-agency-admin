from rest_framework import generics
from .models import CalendarEvent
from .serializers import CalendarEventSerializer

class CalendarEventAPIView(generics.ListAPIView):
    queryset = CalendarEvent.objects.all()
    serializer_class = CalendarEventSerializer
