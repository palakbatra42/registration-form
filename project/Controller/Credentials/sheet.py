import os
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.decorators.http import require_POST
from project.Models.Lead import Lead

try:
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    service_account = None
    build = None


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_FILE = os.path.join(BASE_DIR, 'service.json')

SPREADSHEET_ID = '1LDbyl1CFW_eIpANKK7cd2amVjRoEwRxXCMVGgXyloYk'
SHEET_RANGE = 'Sheet1!A:D'


def Get_service():
    if service_account is None or build is None:
        raise RuntimeError('Google Sheets client libraries are not installed.')

    if not os.path.exists(KEY_FILE):
        raise FileNotFoundError(f'Google service account file not found: {KEY_FILE}')
    
    creds = service_account.Credentials.from_service_account_file(
        KEY_FILE,
        scopes=['https://www.googleapis.com/auth/spreadsheets'],
    )
    return build('sheets', 'v4', credentials=creds)


def add_lead(name, email, phone, source):
    service = Get_service()

    # Get existing data from Google Sheet
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_RANGE,
    ).execute()

    rows = result.get("values", [])

    # Check if email already exists
    for row in rows[1:]:      # Skip header row
        if len(row) > 1 and row[1] == email:
            print(f"{email} already exists in Google Sheet.")
            return

    # Add new row
    new_row = [[name, email, phone, source]]

    response = service.spreadsheets().values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_RANGE,
        valueInputOption="USER_ENTERED",
        body={"values": new_row},
    ).execute()

    return response


def Fetch_lead():
    service = Get_service()
    result = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=SHEET_RANGE,
    ).execute()
    rows = result.get('values', [])
    if not rows:
        return []
    headers = rows[0]
    return [dict(zip(headers, row)) for row in rows[1:]]

def Export_google_sheet(request):
    try:
        leads = Lead.objects.all()

        if not leads.exists():
            messages.info(request, 'No leads found to export.')
            return redirect('Lead:Record')

        for lead in leads:
            add_lead(
                lead.name,
                lead.email,
                lead.phone,
                lead.source,
            )

        messages.success(request, 'Leads exported to Google Sheets successfully.')

    except Exception as exc:
        messages.error(request, f'Unable to export leads to Google Sheets: {exc}')

    return redirect('Lead:Record')


def Sync_lead(request):
    data = Fetch_lead()
    return JsonResponse({'leads': data})
