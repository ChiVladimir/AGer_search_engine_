from bs4 import BeautifulSoup
import requests

#url = 'https://www.avito.ru/moskva_i_mo/mall/zapchasti_i_aksessuary?q=задний амортизатор+Mercedes+GL+164&s=104'
url = 'https://fastfairy.ru/products/category/prinadlezhnosti-kamina'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
#new_doc = UnicodeDammit.detwingle(doc)
content = str(soup.find_all())
print(type(content))
#print(content)
with open('file_1.txt', 'r+') as f:
    f.write(content)





#print(new_doc.decode("utf8"))
# Найти все элементы с тегом <span> и классом 'price'
#content = soup.find_all()
#print(soup.prettify("latin-1"))
#prices = soup.find_all('price', class_='1700')
#for price in prices:
#    print(price.text)
#f.close()