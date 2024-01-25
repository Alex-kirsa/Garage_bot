from googleapiclient.discovery import build
import httplib2
from oauth2client.service_account import ServiceAccountCredentials
from config.conf import sheet_id


class Sheets:
    scopes = ['https://www.googleapis.com/auth/spreadsheets']
    creds_service = ServiceAccountCredentials.from_json_keyfile_name("config/cred.json", scopes).authorize(httplib2.Http())
    service = build('sheets', 'v4', http=creds_service)
    sheet = service.spreadsheets()

    def rewrite_sheet(self, val: list):
        self.service.spreadsheets().values().clear(spreadsheetId=sheet_id, range="Лист1!A2:Z1000").execute()

        self.sheet.values().append(
            spreadsheetId=sheet_id,
            range="Лист1!A2",
            valueInputOption="RAW",
            # insertDataOption="INSERT_ROWS",
            body={'values': val}).execute()

    def read_sheet(self):
        resp = self.sheet.values().batchGet(spreadsheetId=sheet_id, ranges=["Лист1"]).execute()
        return [x for x in resp["valueRanges"][0]["values"]][1:]

    def write_receipt(self, val):
        self.sheet.values().append(
            spreadsheetId=sheet_id,
            range="Оплаты",
            valueInputOption="RAW",
            # insertDataOption="INSERT_ROWS",
            body={'values': val}).execute()

