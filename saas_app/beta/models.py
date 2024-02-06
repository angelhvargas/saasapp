from django.db import models
from django.utils.crypto import get_random_string
from model_utils.models import TimeStampedModel
from saas_app.models.base import BaseModel

def get_code():
    return get_random_string(50)

class Invite(BaseModel):
    code = models.CharField(max_length=50, default=get_code)
    request = models.OneToOneField("Request", on_delete=models.CASCADE)

    def __str__(self):
        return self.code

class Request(BaseModel):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
