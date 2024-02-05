from model_utils.models import TimeStampedModel
from autoslug import AutoSlugField
from slugify import slugify as unicode_slugify
from tinymce.models import HTMLField

from django.db import models
from django.urls import reverse


class Entry(TimeStampedModel):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from="title", slugify=unicode_slugify)
    content = HTMLField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog:entry", kwargs={"slug": self.slug})

    class Meta:
        ordering = ("-created",)
