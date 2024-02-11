# Generated by Django 4.2.10 on 2024-02-08 01:57

import autoslug.fields
from django.db import migrations, models
import slugify


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="entry",
            name="id",
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name="entry",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                editable=False, populate_from="title", slugify=slugify.slugify
            ),
        ),
    ]