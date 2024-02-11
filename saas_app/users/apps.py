# saas_app/users/apps.py
from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = "saas_app.users"

    def ready(self):
        # Import signals to ensure they are connected
        import saas_app.users.signals
