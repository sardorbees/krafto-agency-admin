# orders/models.py

from django.db import models

class Order(models.Model):
    DELIVERY_METHODS = [
        ('delivery', 'Etkazib berish'),
        ('pickup', 'Doʻkondan olib ketish'),
    ]
    DELIVERY_TYPE = [
        ('standard', 'Ertaga yoki keyinroq'),
        ('fast', 'Tez yetkazib berish'),
    ]
    PAYMENT_METHODS = [
        ('payme', 'Payme'),
        ('click', 'Click'),
        ('card', 'Onlayn karta orqali'),
        ('cod', 'Qabul qilinganda'),
        ('installment', 'Muddatli toʻlov'),
    ]

    # Foydalanuvchi ma'lumotlari
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    # Manzil
    region = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True)
    apartment = models.CharField(max_length=100, blank=True)

    # Yetkazib berish va toʻlov
    delivery_method = models.CharField(max_length=20, choices=DELIVERY_METHODS)
    delivery_type = models.CharField(max_length=20, choices=DELIVERY_TYPE)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHODS)

    # Narx
    total_price = models.DecimalField(max_digits=12, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.phone})"
