# saas_app/users/signals.py
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .tasks import subscribe_to_mailing_list  # This is your Celery task


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_registration_mail(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "New Registration",
            message=f"<{instance.email}> has just registered",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.SAAS_INFO_MAIL],
        )


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def user_post_save_receiver(sender, instance, created, **kwargs):
    if created:
        # Queue the subscribe_to_mailing_list task
        subscribe_to_mailing_list.delay(user_pk=instance.pk)
