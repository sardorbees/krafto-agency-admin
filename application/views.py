from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationSerializer
from application.models import Application
from notifications.models import Notification
from django.db.models.signals import post_save
from django.dispatch import receiver

class ApplicationCreateAPIView(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Заявка успешно отправлена!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@receiver(post_save, sender=Application)
def create_notification(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title="Новая заявка",
            message=f"Поступила новая заявка от {instance.full_name} ({instance.email})"
        )

from django.http import JsonResponse
from .models import Application  # твоя модель заявок

def check_new_application(request):
    latest = Application.objects.order_by('-id').first()
    return JsonResponse({'latest_id': latest.id if latest else 0})

