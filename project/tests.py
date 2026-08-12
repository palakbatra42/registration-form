from django.test import SimpleTestCase
from django.urls import reverse


class GoogleSheetExportTests(SimpleTestCase):
    def test_export_google_sheet_route_is_available(self):
        url = reverse("Credentials:export_google_sheet")
        self.assertEqual(url, "/Credentials/export/")
