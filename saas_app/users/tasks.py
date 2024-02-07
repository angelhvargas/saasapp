# saas_app/users/tasks.py
from celery import shared_task
import mailchimp

from django.conf import settings
from django.contrib.auth import get_user_model

@shared_task
def subscribe_to_mailing_list(user_pk, **kwargs):  # pragma: no cover
    User = get_user_model()
    user = User.objects.get(pk=user_pk)
    if getattr(settings, "MAILCHIMP_API_KEY", False):
        m = mailchimp.Mailchimp(settings.MAILCHIMP_API_KEY)
        m.lists.subscribe(
            settings.MAILCHIMP_LIST,
            email={"email": user.email},
            double_optin=False,
            send_welcome=False,
        )
