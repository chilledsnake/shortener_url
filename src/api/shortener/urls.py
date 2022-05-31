from django.urls import path

from src.api.shortener import views

app_name = "shortener"

urlpatterns = [
    path("", views.ShortenerCreateApiView.as_view(), name="create"),
    path("<uuid:uuid>", views.ShortenerRetrieveApiView.as_view(), name="retrieve"),
]
