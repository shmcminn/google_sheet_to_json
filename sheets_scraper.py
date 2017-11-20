from __future__ import print_function

import json
import os
import itertools
import copy

import httplib2
import os

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage


SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'
APPLICATION_NAME = 'Google Sheets API Python Quickstart'

### instructions found here https://developers.google.com/sheets/api/quickstart/python to sync this with your google account
### api docs here https://developers.google.com/sheets/api/reference/rest/

# change these options
# NOTE: ONLY WORKS FOR FILES ON AUTHORIZED ACCOUNT
SPREADSHEET_ID = ""
SHEET_RANGE = "Sheet1"
OUTPUT_FILE = "output.txt"



def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """
    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir,
                                   'sheets.googleapis.com-python-quickstart.json')
    

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        print("missing good credentials")
    return credentials




def main(sheet_name, data_list):
    credentials = get_credentials()
    http = credentials.authorize(httplib2.Http())
    discoveryUrl = ('https://sheets.googleapis.com/$discovery/rest?'
                    'version=v4')
    service = discovery.build('sheets', 'v4', http=http,
                              discoveryServiceUrl=discoveryUrl, cache_discovery = False)

    spreadsheetId = SPREADSHEET_ID
    rangeName = sheet_name
    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheetId, range=rangeName).execute()
    values = result.get('values', [])
    


    if not values:
        print('No data found.')
   
    else:
        for ind, row in enumerate(values):
            if len(row) < len(values[0]):
                row = row + list(itertools.repeat("", len(values[0])-len(row)))
            if ind != 0:
                d = {}
                for ind2, item in enumerate(row): 
                    d[str(values[0][ind2]).replace(" ","_").replace("-", "_").lower()] = item
                data_list.append(d)





result_list = []

main(SHEET_RANGE, result_list)




with open(OUTPUT_FILE, "w") as ofile:
    ofile.write(json.dumps(result_list))
ofile.close()