from sys import argv
import webbrowser
import base64
import requests
import config
import time


module, filename = argv

data = open(filename, 'rb').read()

base64_encoded = base64.b64encode(data).decode('UTF-8')

login = config.USERNAME
password = config.PASSWD
code_templ = 350016735	#int код шаблона (этот шаблон должен быть включен и иметь тип 'Загрузка прайса через API')
url = ""	#да	ссылка на прайс-лист
file_body =	base64_encoded#string содержимое прайс-листа в кодировке base64
file_name = filename#	string имя файла
api_key = config.API

print (login)
print (password)
print (code_templ)
print (url)
print (file_body)
print (file_name)
print (api_key)

response_1 = requests.get('https://api.github.com')
print(response_1.status_code)


response_2 = requests.post(f'https://api.zzap.pro/webservice/datasharing.asmx/UploadTemplatePrice?login={login}'
                          f'&password={password}&code_templ={code_templ}&url={url}&file_body={file_body}'
                          f'&file_name={file_name}&api_key={api_key}')

print(f'https://api.zzap.pro/webservice/datasharing.asmx/UploadTemplatePrice?login={login}&password={password}'
        f'&code_templ={code_templ}&url={url}&file_body={file_body}&file_name={filename}&api_key={api_key}')
print(response_2.status_code)
time.sleep(10)

BASE_URL = "https://api.zzap.pro/webservice/datasharing.asmx/UploadTemplatePrice"
data_to_post = {"login":login,
                "password":password,
                "code_templ":code_templ,
                "url":url,
                "file_body":file_body,
                "file_name":file_name,
                "api_key":api_key}

print(data_to_post)
#exit()
response_3 = requests.post(f"{BASE_URL}/post", json = data_to_post)
print(response_3.status_code)
time.sleep(10)