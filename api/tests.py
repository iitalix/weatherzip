from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient


class WeatherZipTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.valid_zip = "94103"
        self.invalid_zip = "ABCDE"

    def test_zip_code_validation(self):
        """Test that only valid ZIP codes pass validation"""
        from api.serializers import ZipSerializer

        serializer = ZipSerializer(data={"zipcode": self.valid_zip})
        self.assertTrue(serializer.is_valid())

        serializer = ZipSerializer(data={"zipcode": self.invalid_zip})
        self.assertFalse(serializer.is_valid())

    def test_api_response_for_valid_zip(self):
        """Test API endpoint returns data for a valid ZIP code"""
        response = self.client.get(f"/zip-weather/{self.valid_zip}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("maxtemp_f", response.data)
        self.assertIn("mintemp_f", response.data)

    def test_api_response_for_invalid_zip(self):
        """Test API endpoint rejects an invalid ZIP code"""
        response = self.client.get(f"/zip-weather/{self.invalid_zip}/")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
