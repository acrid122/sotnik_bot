import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
#from schedule import every, repeat
from pprint import pprint
#Google Api
CREDENTIALS_F = 'credentials.json'
spreadsheet_id = '1rkB1Ss001HZCFpOoDBBKVBQSzn1UFB7eN9BgwUW6n_o'
credentials = ServiceAccountCredentials.from_json_keyfile_name(
  CREDENTIALS_F,
  ['https://www.googleapis.com/auth/drive',
   'https://www.googleapis.com/auth/spreadsheets']
)
AUTH = credentials.authorize(httplib2.Http())
SERVICE = apiclient.discovery.build('sheets', 'v4', http = AUTH)
#Get Info From Sheet
#@repeat(every().minute.at(":10"))
def getInfoAboutStudents():
  ITEMS_INFO = SERVICE.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    #перед ! указать название листа
    range = 'a8!A:G'
  ).execute()
  return ITEMS_INFO
def getInfoAboutHomeworks():
  ITEMS_HOMEWORK = SERVICE.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    #перед ! указать название листа
    #значение справа от : переставлять 
    range = 'a8!I:BV'
  ).execute()
  return ITEMS_HOMEWORK
