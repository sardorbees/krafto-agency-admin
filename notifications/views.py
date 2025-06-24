from rest_framework import generics
from .models import Notification
from .serializers import NotificationSerializer
from .models import Notification


class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from application.serializers import ApplicationSerializer
from notifications.models import Notification

class ApplicationCreateAPIView(APIView):
    def post(self, request):
        serializer = ApplicationSerializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()

            # 🟢 Внутри метода, где instance уже есть
            Notification.objects.create(
                title="Новая заявка",
                message=f"Поступила новая заявка от {instance.full_name}"
            )

            return Response({"message": "Заявка успешно отправлена!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
from django.http import JsonResponse
from .models import Notification

def latest_notification_id(request):
    latest = Notification.objects.order_by('-id').first()
    return JsonResponse({'id': latest.id if latest else 0})