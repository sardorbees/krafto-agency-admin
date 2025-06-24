from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # покажет username

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at', 'updated_at']
