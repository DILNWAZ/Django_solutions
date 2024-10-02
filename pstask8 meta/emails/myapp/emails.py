from django.core.mail import send_mail
from django.conf import settings
from .models import user 
from rest_framework_simplejwt.tokens import RefreshToken

def send_vrification_email(email):
    try:
        subject = 'Account Verification'
        user = user.objects.get(email=email)

        token = RefreshToken.for_user(user).access_token

        verification_link = f""
    except :