from django.urls import path

from .views import GetZipWeather

urlpatterns = [
    path("zip-weather/<str:zip_code>/", GetZipWeather.as_view(), name="weather-by-zip")
]
