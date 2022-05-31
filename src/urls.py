from django.contrib import admin
from django.urls import include, path

from src.api.shortener import urls as shortener_urls
from swagger.conf import schema_view

urlpatterns = [
    path("", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("admin/", admin.site.urls),
    path("shortener/", include(shortener_urls)),
]
