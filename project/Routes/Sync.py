from django.urls import path
from project.Controller.Credentials import sheet

app_name = "Credentials"

urlpatterns = [
    path("sync/", sheet.Sync_lead, name="sync-leads"),
    path("export/google/", sheet.Export_google_sheet, name="Export_google_sheet"),
]