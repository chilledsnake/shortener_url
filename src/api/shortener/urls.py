from rest_framework.routers import DefaultRouter

from src.api.shortener.views import ShortenerViewSet

app_name = "shortener"

router = DefaultRouter()
router.register(r"", ShortenerViewSet, basename="shortener")
urlpatterns = router.urls
