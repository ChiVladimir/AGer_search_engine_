from bs4 import BeautifulSoup
import pandas as pd
import re
#from IPython.display import HTML
import requests
url_bgn = 'https://www.avito.ru/all/mall/zapchasti_i_aksessuary?q='
url_end =  str(input('Введите запрос для поиска (вместо пробелов необходимо ввести +) >>>'))
url = url_bgn + url_end
print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
item_item = soup.find_all("div", {"data-marker": "catalog-serp"})
#item = item_item[0].find_all("meta")
item_hz = item_item[0].find_all('div', {"data-marker": "item"})
len(item_hz)

test = str(item_item[0])
pos = test.index('iva-item-root-')
print(pos)

indexes = []
for match in re.finditer(r'data-item-id', test):
    indexes.append(match.start())
print(indexes)

data_item_id = []
for i in range(len(indexes)):
    x=indexes[i]+14
    y = x + 10
    data_item_id.append(test[x:y])
print(data_item_id)

soup.find("div", class_ = "items-items-pZX46")