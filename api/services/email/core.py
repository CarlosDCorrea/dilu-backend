from django.core.mail import send_mail
from django.conf import settings


def send(title, subject, template, email):
    send_mail(
        title,
        subject,
        settings.EMAIL_HOST_USER,
        [email],
        html_message=template
    )
