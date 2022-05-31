import uuid

from django.db import models


class ShortUrl(models.Model):

    uuid = models.UUIDField("short", auto_created=True, unique=True, default=uuid.uuid4)
    url = models.URLField("origin url", max_length=1024, unique=True)
