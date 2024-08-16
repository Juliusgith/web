# tasks.py

from celery import shared_task
from django.core.mail import send_mail
from .models import Subscription
from datetime import datetime, timedelta

@shared_task
def send_subscription_reminder(email, reminder_type):
    if reminder_type == "first":
        subject = 'Monthly Subscription Reminder'
        message = 'Please visit our website to make your monthly payment.'
    elif reminder_type == "second":
        subject = 'Final Subscription Reminder'
        message = 'This is a final reminder to make your monthly payment.'
    
    send_mail(
        subject,
        message,
        'from@example.com',
        [email],
        fail_silently=False,
    )

def schedule_reminders(subscription):
    now = datetime.now()
    first_reminder_date = (now + timedelta(days=25)).replace(hour=0, minute=0, second=0, microsecond=0)
    second_reminder_date = (now + timedelta(days=(1 if now.day <= 25 else (25 - now.day + 1)))).replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    
    send_subscription_reminder.apply_async((subscription.email, "first"), eta=first_reminder_date)
    send_subscription_reminder.apply_async((subscription.email, "second"), eta=second_reminder_date)
