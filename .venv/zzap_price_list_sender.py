#-*- coding: UTF-8 -*-

from sys import argv
import webbrowser
import base64
import requests
import config
import asyncio

BASE_URL = "https://api.zzap.pro/webservice/datasharing.asmx/UploadTemplatePrice"

module, filename = argv

data = open(filename, 'rb').read()

base64_encoded = base64.b64encode(data).decode('UTF-8')

login = config.USERNAME
password = config.PASSWD
code_templ = 350016735	#int код шаблона (этот шаблон должен быть включен и иметь тип 'Загрузка прайса через API')
url = ""  # Пусто для отправки данных в file_body
file_body =	base64_encoded #string содержимое прайс-листа в кодировке base64
file_name = filename
api_key = config.API

data_to_post = {"login":login,
                "password":password,
                "code_templ":code_templ,
                "url":url,
                "file_body":file_body,
                "file_name":file_name,
                "api_key":api_key}

print(data_to_post)
#exit()
response = requests.post(f"{BASE_URL}/post", json = data_to_post)

#print(response.status_code, response.json())