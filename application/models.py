from django.db import models

class Application(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    email = models.EmailField("Email")
    message = models.TextField("Сообщение")
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.email}"
    

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'

