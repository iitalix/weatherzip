import requests
from decouple import config
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ZipSerializer


class GetZipWeather(APIView):
    def post(self, request):
        serializer = ZipSerializer(data=request.data)
        WEATHER_API_URL = "http://api.weatherapi.com/v1/forecast.json"
        API_KEY = config("SECRET_KEY")

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # If the serializer is valid, we can access the validated data
        zipcode = serializer.validated_data["zipcode"]

        try:
            response = requests.get(
                WEATHER_API_URL,
                params={
                    "key": API_KEY,
                    "q": zipcode,
                    "days": 1,  # Include forecast for one day
                },
            )

            # Print full API response
            # print("WeatherAPI Response:", response.json())

            if response.status_code == 200:
                weather_data = response.json()
                forecast = weather_data.get("forecast", {}).get("forecastday", [{}])[0]

                weather_summary = {
                    "city": weather_data["location"]["name"],
                    "state": weather_data["location"]["region"],
                    "maxtemp_f": forecast.get("day", {}).get("maxtemp_f"),
                    "mintemp_f": forecast.get("day", {}).get("mintemp_f"),
                }

                print(
                    "Weather Summary:", weather_summary
                )  # Print the processed weather summary
                return Response(weather_summary, status=status.HTTP_200_OK)

            else:
                return Response(
                    {
                        "error": "Failed to fetch weather data.",
                        "details": response.json(),
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

        except requests.exceptions.RequestException as e:
            return Response(
                {
                    "error": "An error occurred while fetching weather data.",
                    "details": str(e),
                },
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
