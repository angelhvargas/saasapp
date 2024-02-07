# saas_app/users/apps.py

from django.apps import AppConfig
from django.db.models.signals import post_save
from django.conf import settings

class UsersConfig(AppConfig):
    name = 'saas_app.users'

    def ready(self):
        # Importing model classes
        from .models import User

        # Importing signal handlers locally to avoid cyclic import
        from .signals import send_registration_mail, subscribe_to_mailing_list

        # Connecting signal handlers
        post_save.connect(send_registration_mail, sender=User)
        post_save.connect(subscribe_to_mailing_list, sender=User)
