from rest_framework import serializers
from user.models import *

from shop.serializers import ProductListSerializer



class CustomUserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email",
                  "password")

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = CustomUser.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class CustomUserUpdateSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("username", "first_name", "last_name", "email",
                  "phone_number", "photo", "password")

    def get_photo(self, obj):
        if obj.photo:
            return obj.photo.url
        return None


class CustomUserSerializer(serializers.ModelSerializer):
    photo = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "phone_number",
                  "username", "photo")

    def get_photo(self, obj):
        if obj.photo:
            return obj.photo.url
        return None


class CartItemSerializer(serializers.ModelSerializer):
    product = ProductListSerializer()

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'product_final_price']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ['id', 'user', 'items', 'total_price', 'created_at']
        read_only_fields = ['user', 'total_price', 'created_at']