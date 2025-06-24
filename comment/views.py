from rest_framework import viewsets, permissions
from .models import Comment
from .serializers import CommentSerializer

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Разрешить редактирование только владельцу комментария.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    def get_queryset(self):
        # Показываем комментарии только текущего пользователя (или всех, если нужно)
        return Comment.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
