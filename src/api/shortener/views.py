from rest_framework import mixins, viewsets

from src.api.shortener.models import ShortUrl
from src.api.shortener.serializers import ShortUrlSerializer


class ShortenerViewSet(
    mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet
):

    serializer_class = ShortUrlSerializer
    queryset = ShortUrl.objects.all()
    lookup_field = "uuid"
