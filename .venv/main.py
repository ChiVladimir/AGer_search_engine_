from bs4 import BeautifulSoup
import pandas as pd
import re
#from IPython.display import HTML
import requests


# Нырок 1, в список
url_bgn = 'https://www.avito.ru/all/mall/zapchasti_i_aksessuary?q='
url_end =  str(input('Введите запрос для поиска (вместо пробелов необходимо ввести +) >>>'))
url = url_bgn + url_end
#print(url)
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
item_item = soup.find_all("div", {"data-marker": "catalog-serp"})

quest = str(item_item[0])

indexes = []
for match in re.finditer(r'data-item-id', quest):
    indexes.append(match.start())
#print(indexes)

data_item_id = []
for i in range(len(indexes)):
    x=indexes[i]+14
    y = x + 10
    data_item_id.append(quest[x:y])
#print(data_item_id)

# Нырок 2, в заметки

url_chld = 'https://www.avito.ru/' + data_item_id[0]
#print(url_chld)
response = requests.get(url_chld)
soup = BeautifulSoup(response.text, 'lxml')
#Название
name_drt = str(soup.find("h3", class_ = "styles-module-root-W_crH styles-module-root-o3j6a styles-module-size_xl"
                                        "-smy1L styles-module-size_xl_dense-Qxvdb styles-module-size_xl-TN4iZ styles"
                                        "-module-size_dense-cyeE0 stylesMarningNormal-module-root-_BXZU stylesMarning"
                                        "Normal-module-header-xl-b8TLy styles-module-root_top-SRn_H styles-module-"
                                        "margin-top_6-cRzNx styles-module-root_bottom-oEs9f styles-module-margin"
                                        "-bottom_10-povCj"))
point_from = name_drt.index('">')
point_to = name_drt.index('</h3')
name = name_drt[point_from + 2:point_to]
print(name)

#Цена

price_drt = str(soup.find("span", class_ = "styles-module-size_xxxxl-f_FvC"))
point_from = price_drt.index('tent="')
point_to = price_drt.index('" data')
price = price_drt[point_from + 6:point_to]
print(price)

#Продавец

company_name_drt = str(soup.find("h3", class_ = "styles-module-root-W_crH styles-module-root-o3j6a styles-module-"
                                                "size_xl-smy1L styles-module-size_xl_dense-Qxvdb styles-module-size_xl"
                                                "_compensated-VsNpt styles-module-size_xl-TN4iZ styles-module-ellipsis"
                                                "-XeCfh styles-module-size_dense-cyeE0 stylesMarningNormal-module-"
                                                "root-_BXZU stylesMarningNormal-module-header-xl-b8TLy"))
#print(company_name_drt)
point_from = company_name_drt.index('="">')
point_to = company_name_drt.index('</span></a></h3>')
company_name = company_name_drt[point_from + 4:point_to]
print(company_name)

#seller_info_rating

seller_class_drt = str(soup.find("div", class_ = "style-seller-info-rating-xHI5T seller-info-rating"))
point_from = seller_class_drt.index('m-n6S6Y">')
seller_info_rating = seller_class_drt[point_from + 9:point_from + 12]
print(seller_info_rating)

#seller_class

seller_class_drt = str(soup.find("a", class_ = "styles-module-root-iSkj3 styles-module-size_m-n6S6Y styles-module"
                                               "-root_noVisited-qJP5D styles-module-root_preset_black-PbPLe"))
point_to = seller_class_drt.index('</a>')
point_from = seller_class_drt.index('">')
seller_responce = seller_class_drt[point_from + 2:point_to]
print(seller_responce)

#speed_of_responce

speed_of_responce_drt = str(soup.find("div", class_ = "style-sellerInfoReplyTime-EdRsf"))
point_from = speed_of_responce_drt.index('pH9s3">')
point_to = speed_of_responce_drt.index('</p></div>')
speed_of_responce = speed_of_responce_drt[point_from + 7:point_to]
print(speed_of_responce)

#address

address_drt = str(soup.find("span", class_ = "style-item-address__string-wt61A"))
point_from = address_drt.index('-wt61A">')
point_to = address_drt.index('</span>')
address = address_drt[point_from + 8:point_to]
print(address)

#Вывод в таблицу

data = {'Позиция':'', 'ID':data_item_id[0], 'Заголовок':name, 'Цена':price, 'Просм. всего':'', 'Просм. сегодня':'',
        'Продвижение':'', 'Время поднятия':'', 'Фото (шт)':'', 'Текст':'', 'Кол-во знаков':'', 'Доставка':'',
        'Имя продавца':company_name, 'ID продавца':'', 'Тип продавца':'', 'Скорость ответа':speed_of_responce,
        'Рейтинг продавца':seller_info_rating, 'Отзывов продавца':seller_responce, 'Адрес':address, 'Ссылка':'',
        'Фото (ссылки)':''}

output_table = pd.DataFrame(data, index=[0])
print (output_table)