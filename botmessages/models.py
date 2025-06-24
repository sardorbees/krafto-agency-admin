from django.db import models
from .telegram import send_telegram_message

class Message(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=50)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)
        if is_new:
            send_telegram_message(
                f"📩 <b>У вас новое сообщение от Django!</b>\n\n"
                f"<b>👤 Имя:</b> {self.full_name}\n"
                f"<b>📞 Телефон:</b> {self.phone}\n"
                f"<b>📧 Email:</b> {self.email or '—'}\n"
                f"<b>💬 Сообщение:</b> {self.text}"
            )

    def __str__(self):
        return f"{self.full_name} — {self.phone}"
