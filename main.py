import gspread
from google.oauth2.service_account import Credentials

scopes = ["https://www.googleapis.com/auth/spreadsheets"]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)

sheet_id = "1kky6A1l-JT0St3AB-0-pAzIiCp8ynD8aRMweH3upZV8"
workbook = client.open_by_key(sheet_id)

def func():
    pass