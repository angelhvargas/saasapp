from __future__ import absolute_import
import os
from celery import Celery

from django.apps import AppConfig
from django.conf import settings


if not settings.configured:
    # set the default Django settings module for the 'celery' program.
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "config.settings.development"
    )  # pragma: no cover


app = Celery("saas_app")


class CeleryConfig(AppConfig):
    name = "saas_app.taskapp"
    verbose_name = "Celery Config"

    def ready(self):  # pragma: no cover
        # Using a string here means the worker will not have to
        # pickle the object when using Windows.
        app.config_from_object("django.conf:settings")
        app.autodiscover_tasks(lambda: settings.INSTALLED_APPS, force=True)

        if hasattr(settings, "RAVEN_CONFIG"):
            # Celery signal registration
            from raven import Client as RavenClient
            from raven.contrib.celery import register_signal as raven_register_signal
            from raven.contrib.celery import (
                register_logger_signal as raven_register_logger_signal,
            )

            raven_client = RavenClient(dsn=settings.RAVEN_CONFIG["DSN"])
            raven_register_logger_signal(raven_client)
            raven_register_signal(raven_client)


@app.task(bind=True)
def debug_task(self):
    print("Request: {0!r}".format(self.request))  # pragma: no cover
