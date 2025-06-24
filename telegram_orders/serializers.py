from rest_framework import serializers
from .models import TelegramRequest
from .models import TelegramUser

class TelegramRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramRequest
        fields = '__all__'

# serializers.py
from rest_framework import serializers
from .models import TelegramUser

class TelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = '__all__'

