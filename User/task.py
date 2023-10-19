from celery import shared_task
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.urls import reverse
from django.core.mail import send_mail
from User.models import User


@shared_task
def send_password_reset_email(user_id, reset_url):
    
    user = User.objects.get(pk=user_id)
    subject = 'Password Reset'
    message = f'Click the following link to reset your password: {reset_url}'
    send_mail(subject, message, 'reset_email@example.com', [user.email])