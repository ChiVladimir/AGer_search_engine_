from bs4 import BeautifulSoup
import pandas as pd
import re
#from IPython.display import HTML
import requests
import os
from fake_useragent import UserAgent
#import json

# Нырок 1, в список
url_bgn = 'https://www.avito.ru/all/mall/zapchasti_i_aksessuary?q='
print("\nВНИМАНИЕ! Перед запуском модуля необходимо включить VPN\n")
#url_end =  str(input('Введите запрос для поиска (вместо пробелов необходимо ввести +) >>>'))
#url = url_bgn + url_end
url = 'https://www.avito.ru/all/mall/zapchasti_i_aksessuary?q=Компрессор+пневмоподвески+Mercedes+GL+166'
print(url)
response = requests.get(url, headers={'User-Agent': UserAgent().safari})
soup = BeautifulSoup(response.text, 'lxml')
name = 'soup.txt'
file = open(name, 'a')
file.write(str(soup))
file.close()
item_item = soup.find_all("div", {"data-marker": "catalog-serp"})
name = 'item_item.txt'
file = open(name, 'a')
file.write(str(item_item))
file.close()
quest = str(item_item[0])

indexes = []
for match in re.finditer(r'data-item-id', quest):
    indexes.append(match.start())
print(indexes)

data_item_id = []
for i in range(len(indexes)):
    x=indexes[i]+14
    y = x + 10
    data_item_id.append(quest[x:y])
print(data_item_id)
name = 'data_item_id.txt'
with open(name, "w+") as fp:
    data_to_write = '\n'.join(data_item_id)
    file.write(data_to_write)
    file.close()


