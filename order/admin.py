# orders/admin.py

from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone', 'delivery_method', 'payment_method', 'total_price', 'created_at')
    list_filter = ('delivery_method', 'payment_method')
    search_fields = ('first_name', 'last_name', 'phone')
