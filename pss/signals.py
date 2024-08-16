# signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Subscription
from .tasks import schedule_reminders

@receiver(post_save, sender=Subscription)
def subscription_created(sender, instance, created, **kwargs):
    if created:
        schedule_reminders(instance)
