from rest_framework import serializers
from rest_framework.reverse import reverse

from src.api.shortener.models import ShortUrl


class ShortUrlSerializer(serializers.ModelSerializer):
    short_url = serializers.SerializerMethodField()

    class Meta:
        model = ShortUrl
        fields = ("url", "short_url")

    def get_short_url(self, obj):
        url = reverse(
            "shortener:retrieve",
            kwargs={"uuid": obj.uuid},
            request=self.context.get("request", ""),
        )
        return url
