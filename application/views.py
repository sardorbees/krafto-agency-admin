from rest_framework import generics
from .models import ApplicationForm
from .serializers import ApplicationFormSerializer
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.conf import settings

class ApplicationFormCreateAPIView(generics.CreateAPIView):
    queryset = ApplicationForm.objects.all()
    serializer_class = ApplicationFormSerializer
    
    
TELEGRAM_TOKEN = '7614226832:AAGUGKTBy0J5HpBj9Pyuh4uUIco2GTmWADE'
CHAT_ID = '7139975148'  # можно ID канала или пользователя

@api_view(['POST'])
def send_telegram_message(request):
    data = request.data
    text = (
        f"📥 Новая заявка от Сайта Kracto-Agency:\n\n"
        f"👤 ФИО: {data.get('full_name')}\n"
        f"📱 Телефон: {data.get('phone_number')}\n"
        f"✉️ Email: {data.get('email') or '—'}\n"
        f"🛠 Услуга: {data.get('service_type')} > {data.get('subservice_type')}\n"
        f"💼 Тариф: {data.get('tariff')}\n"
        f"💰 Цена: {data.get('price')}\n"
        f"📝 Комментарий: {data.get('comment') or '—'}"
    )
    
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": text, "parse_mode": "HTML"}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        return Response({"status": "ok"})
    else:
        return Response({"status": "error", "message": response.text}, status=500)
