from django.core.exceptions import ValidationError
from django.test import SimpleTestCase
from django.urls import reverse

from project.Models.Lead import Lead


class GoogleSheetExportTests(SimpleTestCase):
    def test_export_google_sheet_route_is_available(self):
        url = reverse("Credentials:Export_google_sheet")
        self.assertEqual(url, "/Credentials/export/google/")


class LeadPhoneValidationTests(SimpleTestCase):
    def test_phone_must_have_exactly_10_digits(self):
        valid_lead = Lead(name="Test User", email="valid@example.com", phone=1234567890, source="Web")
        valid_lead.full_clean()

        invalid_lead = Lead(name="Test User", email="invalid@example.com", phone=12345678901, source="Web")
        with self.assertRaises(ValidationError):
            invalid_lead.full_clean()
