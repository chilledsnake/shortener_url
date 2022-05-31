from rest_framework import generics

from src.api.shortener.models import ShortUrl
from src.api.shortener.serializers import ShortUrlSerializer


class ShortenerCreateApiView(generics.CreateAPIView):
    serializer_class = ShortUrlSerializer


class ShortenerRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ShortUrlSerializer
    queryset = ShortUrl.objects.all()
    lookup_field = "uuid"
