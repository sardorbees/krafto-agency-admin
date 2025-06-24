from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TelegramRequestSerializer

class TelegramBotRequestView(APIView):
    def post(self, request):
        serializer = TelegramRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Заявка сохранена'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views.py
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import TelegramUser
from .serializers import TelegramUserSerializer

class TelegramUserCreateOrUpdateView(APIView):
    def post(self, request, *args, **kwargs):
        telegram_id = request.data.get("telegram_id")
        if not telegram_id:
            return Response({"error": "telegram_id is required"}, status=400)

        full_name = request.data.get("full_name", "")
        username = request.data.get("username", "")

        user, created = TelegramUser.objects.get_or_create(telegram_id=telegram_id)

        if created:
            user.full_name = full_name
            user.username = username
            user.is_welcomed = True
            user.save()
            serializer = TelegramUserSerializer(user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "User already exists"}, status=status.HTTP_200_OK)

