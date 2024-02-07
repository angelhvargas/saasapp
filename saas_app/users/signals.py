# saas_app/users/signals.py

from django.core.mail import send_mail
from django.conf import settings

def send_registration_mail(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "New Registration",
            message="{email} has just registered".format(email=instance.email),
            from_email=getattr(settings, "DEFAULT_FROM_EMAIL"),
            recipient_list=[settings.SAAS_INFO_MAIL],
        )

def subscribe_to_mailing_list(sender, instance, created, **kwargs):
    if created:
        # Local import within the signal handler
        from .tasks import subscribe_to_mailing_list
        subscribe_to_mailing_list.delay(user_pk=instance.pk)
