import gspread
from google.oauth2.service_account import Credentials


def upload_to_sheets(data, sheet_id):
    scopes = ["https://www.googleapis.com/auth/spreadsheets"]
    creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
    client = gspread.authorize(creds)
    sheet = client.open_by_key(sheet_id).get_worksheet(0)

    # cleaning old data and loading new data (with headers)
    sheet.clear()
    sheet.update([data.columns.values.tolist()] + data.values.tolist())
    print("✅ Data succesfully loaded into Google Sheets")
