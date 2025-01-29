import requests
from decouple import config
from django.core.cache import cache
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ZipSerializer


class GetZipWeather(APIView):
    def get(self, request, zip_code):
        WEATHER_API_URL = "http://api.weatherapi.com/v1/forecast.json"
        API_KEY = config("SECRET_KEY")

        # Use the serializer to validate the ZIP code
        serializer = ZipSerializer(data={"zipcode": zip_code})

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Check if the data is already cached
        cache_key = f"weather_{zip_code}"
        cached_data = cache.get(cache_key)

        if cached_data:
            print("Returning cached data")
            return Response(cached_data, status=status.HTTP_200_OK)

        try:
            # Fetch weather data from the WeatherAPI
            response = requests.get(
                WEATHER_API_URL,
                params={
                    "key": API_KEY,
                    "q": zip_code,
                    "days": 1,  # Include forecast for one day
                },
            )

            if response.status_code == 200:
                weather_data = response.json()
                forecast = weather_data.get("forecast", {}).get("forecastday", [{}])[0]

                weather_summary = {
                    "city": weather_data["location"]["name"],
                    "state": weather_data["location"]["region"],
                    "maxtemp_f": forecast.get("day", {}).get("maxtemp_f"),
                    "mintemp_f": forecast.get("day", {}).get("mintemp_f"),
                }

                # Cache weather summary for 1 hour (3600 seconds)
                cache.set(cache_key, weather_summary, timeout=3600)

                print("Returning new data and caching it")
                return Response(weather_summary, status=status.HTTP_200_OK)

            else:
                return Response(
                    {
                        "error": "Failed to fetch weather data. Please ensure the ZIP code is valid.",
                        "details": response.json(),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except requests.exceptions.RequestException as e:
            return Response(
                {
                    "error": "Something went wrong on our end. Please try again later or contact support.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
