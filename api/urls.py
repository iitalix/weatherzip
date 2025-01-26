from django.urls import path
from .views import GetZipWeather

urlpatterns = [
  path('zip-weather/', GetZipWeather.as_view(), name='weather-by-zip')
]