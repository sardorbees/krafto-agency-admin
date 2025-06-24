# telegram_notify/models.py
from django.db import models
import requests
from django.conf import settings

class TelegramMessage(models.Model):
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def send_to_telegram(self):
        token = settings.TELEGRAM_BOT_TOKEN
        chat_id = settings.TELEGRAM_CHAT_ID
        url = f"https://api.telegram.org/bot{token}/sendMessage"
        data = {
            'chat_id': chat_id,
            'text': self.message
        }
        try:
            response = requests.post(url, data=data)
            response.raise_for_status()  # проверка на ошибки
        except requests.RequestException as e:
            print("Ошибка при отправке в Telegram:", e)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.send_to_telegram()

    def __str__(self):
        return f"Сообщение от {self.sent_at.strftime('%Y-%m-%d %H:%M')}"
    

class Meta:
    verbose_name = 'Телеграмной сообщение'
    verbose_name_plural = 'Телеграмной сообщение'
