# app_name/signals.py

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Site'
        message = 'Thank you for registering on our site.'
        sender_email = 'your@email.com'  # Your email address
        recipient_email = instance.email
        print(f'mail sent to { recipient_email }')
        # send_mail(subject, message, sender_email, [recipient_email])
