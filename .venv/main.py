from bs4 import BeautifulSoup
import pandas as pd
#from IPython.display import HTML
import requests
url_bgn = 'https://www.avito.ru/all/mall/zapchasti_i_aksessuary?q='
url_end =  str(input('Введите запрос для поиска (вместо пробелов необходимо ввести +) >>>'))
url = url_bgn + url_end
print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.find_all("div", {"data-marker": "catalog-serp"}))