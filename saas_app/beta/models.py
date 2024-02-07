from model_utils.models import TimeStampedModel

from django.db import models
from django.utils.crypto import get_random_string


def get_code():
    return get_random_string(50)


class Invite(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=50, default=get_code)
    request = models.OneToOneField("Request", on_delete=models.CASCADE)

    def __str__(self):
        return self.code


class Request(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
