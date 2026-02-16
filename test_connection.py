import gspread
from google.oauth2.service_account import Credentials
import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


def test_google_sheets():
    try:
        # Define scopes
        scopes = ["https://www.googleapis.com/auth/spreadsheets"]

        # Load credentials
        creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
        client = gspread.authorize(creds)

        # Try to open the sheet by ID from .env
        sheet_id = os.getenv("GOOGLE_SHEET_ID")
        sheet = client.open_by_key(sheet_id)

        print(f"✅ Success! Connected to spreadsheet: {sheet.title}")
    except Exception as e:
        print(f"❌ Connection failed: {e}")


if __name__ == "__main__":
    test_google_sheets()