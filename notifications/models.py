from django.db import models

class Notification(models.Model):
    title = models.CharField("Заголовок", max_length=255)
    message = models.TextField("Сообщение")
    is_read = models.BooleanField("Прочитано", default=False)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return self.title

class Meta:
    verbose_name = 'Сообщение'
    verbose_name_plural = 'Сообщение'