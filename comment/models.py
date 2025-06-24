from django.db import models
from django.conf import settings

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments',)
    text = models.TextField("Коментария написать")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.user.username} at {self.created_at}'
    

class Meta:
    verbose_name = 'Коментария пользовтель'
    verbose_name_plural = 'Коментария пользовтель'

