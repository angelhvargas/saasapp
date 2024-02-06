from django.db import models
from model_utils.models import TimeStampedModel

class BaseModel(TimeStampedModel):
    # If you have additional common fields, define them here

    class Meta:
        abstract = True
        ordering = ['id']
