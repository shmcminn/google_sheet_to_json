# Scrape Google Sheets to write local JSON file

Uses the Google Sheets API to access a spreadsheet and write it as JSON, which can then be accessed by other scripts, web apps, etc.

IMPORTANT: Follow instruction steps one and two [here](https://developers.google.com/sheets/api/quickstart/python) to have your authorization key stored in ~/.credentials. This is required to access your sheet via the API.

Modify the SPREADSHEET_ID, SHEET_RANGE and OUTPUT_FILE variables in the python script with the following information  before running it: 

  * SPREADSHEET ID ==> long string found in Goolge sheet url
  * SHEET_RANGE ==> tabs or ranges you want to acccess in the document
  * OUTPUT_FILE ==> name of file you want to write to

Required libraries are listed in requirements.txt