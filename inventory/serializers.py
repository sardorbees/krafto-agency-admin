# inventory/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    available_quantity = serializers.ReadOnlyField()

    class Meta:
        model = Product
        fields = ['id', 'name', 'total_quantity', 'sold_this_week', 'available_quantity', 'is_active']
