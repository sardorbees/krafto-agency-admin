from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import ApplicationForm

@receiver(post_save, sender=ApplicationForm)
def create_notification_on_new_application(sender, instance, created, **kwargs):
    if created:
        print(f"✅ Новая заявка от: {instance.full_name}")
        if instance.email:
            print(f"📧 Email: {instance.email}")