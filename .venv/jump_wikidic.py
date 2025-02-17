from bs4 import BeautifulSoup
import pandas as pd
import re
#from IPython.display import HTML
import requests
import os
from fake_useragent import UserAgent

# Нырок 1, получаем слово\фразу, делаем выборку по слову\фразе и ее элементам

def extractor(data_item_query):

    url_chld = 'https://ru.wiktionary.org/wiki/' + data_item_query
    print(url_chld)
    response = requests.get(url_chld, headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(response.text, 'html.parser')
    name = data_item_query + '.txt'
    file = open(name, 'w+')
    file.write(str(soup))
    file.close()

    item = soup.find("table", class_ = "wikitable mw-collapsible mw-collapsed")

#Шаблон
    pattern_name = data_item_query
    print(pattern_name)

#Корень и источник(если есть)

    root_wiki_dirt = str(soup.find("th", style="background-color: #efefef; text-align:left; "
                                               "border-right:0; font-size: 95%; font-weight: bold; "
                                               "padding-left:5px;"))
    print(root_wiki_dirt)
    point_from = root_wiki_dirt.index('с корнем <i>')
    point_to = root_wiki_dirt.index('- <')
    root_wiki = root_wiki_dirt[point_from + 12:point_to + 2]
    print(root_wiki)
# source
    source_drt = item.find("span", class_="source")
    source = str(source_drt.text)[1:-1]
    print(source)

#Словарь - Часть речи:[Слово]
    dict = item.find("td", class_="block-body")
    word_dict = {}
    for blc_part_of_speech in dict.find_all("li"):
        words = []
        part_of_speech = str(blc_part_of_speech.span)[6:-8]
        for link in blc_part_of_speech.find_all("a"):
            words.append(link.text)
        word_dict[part_of_speech] = words

    print(word_dict)

#Вывод в таблицу

    data = {'Шаблон': pattern_name, 'Корень Wiktionary': root_wiki, 'Источник(если указан)': source,
            'Части речи и слова': [word_dict]}
    print(data)
    df = pd.DataFrame(data, index=[1])
    pd.DataFrame(data, index=[1])
    # df.to_csv("/Users/vladimirchi/Downloads/data.csv", index=False)
    df.to_csv("data.csv", index=False)


# name = 'List_of_root_morphemes.txt'
#
# data_item_id = list
# with open(name, 'r', encoding='utf-8') as file:
#     data_item_id = file.readlines()
#     print(len(data_item_id), type(data_item_id))

extractor("Шаблон:родств:прав")
extractor("Шаблон:родств:акт")