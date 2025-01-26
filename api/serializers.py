# Used to serialize and deserialize data for API responses
# DRF uses serializers to transform complex data into JSON and vice versa

from rest_framework import serializers

# class WelcomeMessageSerializer(serializers.Serializer):
#   message = serializers.CharField(max_length=100)


# class WeatherDataSerializer(serializers.Serializer):
#   city = serializers.CharField(max_length=100)
#   temperature = serializers.FloatField()
#   description = serializers.CharField(max_length=200)


# class ZipSerializer(serializers.Serializer):
#   zipcode = serializers.CharField(
#     max_length=5,
#     validators=[
#       RegexValidator(
#         regex=r'^\d{5}$',
#         message="Enter a valid 5-digit ZIP code (e.g., 12345)."
#       )
#     ]
#   )


class ZipSerializer(serializers.Serializer):
    zipcode = serializers.CharField(max_length=5)

    def validate_zipcode(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("ZIP code must contain only digits.")
        if len(value) != 5:
            raise serializers.ValidationError("ZIP code must be exactly 5 digits long.")
        return value
