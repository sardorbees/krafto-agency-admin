from django.db import models

class TelegramRequest(models.Model):
    LANGUAGE_CHOICES = [
        ('ru', 'Русский'),
        ('uz', 'O‘zbekcha'),
    ]

    TARIFF_CHOICES = [
        ('standard', 'Стандарт'),
        ('premium', 'Премиум'),
    ]

    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=50)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    service = models.CharField(max_length=100)
    subservice = models.CharField(max_length=100)
    tariff = models.CharField(max_length=20, choices=TARIFF_CHOICES)
    price = models.CharField(max_length=100, default='Договорная')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.service}"
    

class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(unique=True)
    full_name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, blank=True)
    is_welcomed = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.telegram_id} - {self.full_name or 'no_name'}"

