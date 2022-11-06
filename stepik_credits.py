import requests
import json
from stepik_res import client_id_pr
from stepik_res import client_secret_pr
#Stepik info
def stepikAuthAndRetAmount():
  client_id = client_id_pr
  client_secret = client_secret_pr
  auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
  response = requests.post('https://stepik.org/oauth2/token/',
                           data={'grant_type': 'client_credentials'},
                           auth=auth)
  token = response.json().get('access_token', None)
  if not token:
      print('Unable to authorize with provided credentials')
      exit(1)
  #id класса - последний пять цифр ссылки в след. строчке. Чтобы достать его переходим на Stepik в классы,
  #выбираем нужный. В ссылке будут нужные пять цифр перед /gradebook
  class_api_call = 'https://stepik.org/api/classes/37459'
  classes = requests.get(class_api_call, headers = {'Authorization': 'Bearer '+ token}).json()
  return classes['classes'][0]['students_count']
