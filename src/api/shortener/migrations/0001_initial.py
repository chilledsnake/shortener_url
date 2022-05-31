# Generated by Django 4.0.4 on 2022-05-30 14:21

import uuid

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ShortUrl",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "uuid",
                    models.UUIDField(
                        auto_created=True,
                        default=uuid.uuid4,
                        unique=True,
                        verbose_name="short",
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        max_length=1024, unique=True, verbose_name="origin url"
                    ),
                ),
            ],
        ),
    ]