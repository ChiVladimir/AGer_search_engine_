from sys import argv
import webbrowser
import base64
import requests
import config
import time
import json


module, filename = argv

data = open(filename, 'rb').read()

base64_encoded = base64.b64encode(data).decode('UTF-8')

login = config.USERNAME
password = config.PASSWD
code_templ = 350016735	#int код шаблона (этот шаблон должен быть включен и иметь тип 'Загрузка прайса через API')
url = ""	#ссылка на прайс-лист - не нужна для прямого обращения через API, содержащим file_body base64_encoded
file_body = base64_encoded #string содержимое прайс-листа в кодировке base64
file_name = filename#	string имя файла
api_key = config.API
#
# print (login)
# print (password)
# print (code_templ)
# print (url)
# print (file_body)
# print (file_name)
# print (api_key)

BASE_URL = "https://api.zzap.pro/webservice/datasharing.asmx/UploadTemplatePrice"
data_to_post = {"login":login,
                "password":password,
                "code_templ":code_templ,
                "url":url,
                "file_body":file_body,
                "file_name":file_name,
                "api_key":api_key}


response_3 = requests.post(BASE_URL, json = data_to_post)
#print(response_3.status_code)
#time.sleep(10)