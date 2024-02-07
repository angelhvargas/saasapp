from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Assuming top-level import doesn't cause cyclic import issues
from saas_app.users.tasks import subscribe_to_mailing_list

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_registration_mail(sender, instance, created, **kwargs):
    if created:
        send_mail(
            "New Registration",
            message=f"{instance.email} has just registered",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.SAAS_INFO_MAIL],
        )

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def subscribe_user_to_mailing_list(sender, instance, created, **kwargs):
    if created:
        subscribe_to_mailing_list.delay(user_pk=instance.pk)
