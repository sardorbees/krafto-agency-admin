from django.db import models

class ApplicationForm(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)
    service_type = models.CharField(max_length=100)         # напр. веб-сайт
    subservice_type = models.CharField(max_length=100)      # напр. landing page
    tariff = models.CharField(max_length=100)               # стандарт / премиум
    price = models.CharField(max_length=50)                 # напр. договорная
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} | {self.service_type} | {self.phone_number}"
