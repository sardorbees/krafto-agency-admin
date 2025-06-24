from django.db.models.signals import post_save
from django.dispatch import receiver
from application.models import Application
from notifications.models import Notification

@receiver(post_save, sender=Application)
def create_notification_on_new_application(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            title="Новая заявка",
            message=f"Поступила новая заявка от {instance.full_name} ({instance.email})"
        )
