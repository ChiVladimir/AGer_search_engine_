from posixpath import split
from pwd import struct_passwd
import time
from bs4 import BeautifulSoup
import pandas as pd
import re
#from IPython.display import HTML
import requests
import os
from fake_useragent import UserAgent
from database import filling_words

# Нырок 1, получаем слово\фразу, делаем выборку по слову\фразе и ее элементам

def extractor(data_item_query):

    url_chld = 'https://ru.wiktionary.org/wiki/' + data_item_query
#    print(url_chld)
    response = requests.get(url_chld, headers={'User-Agent': UserAgent().chrome})
    soup = BeautifulSoup(response.text, 'html.parser')
    # name = data_item_query + '.txt'
    # file = open(name, 'w+')
    # file.write(str(soup))
    # file.close()

    item = soup.find("table", class_ = "wikitable mw-collapsible mw-collapsed")

#Шаблон
    pattern_name = data_item_query
#    print(pattern_name)

#Корень и источник(если есть)

    root_wiki_dirt = str(soup.find("th", style="background-color: #efefef; text-align:left; "
                                               "border-right:0; font-size: 95%; font-weight: bold; "
                                               "padding-left:5px;"))
#    print("root_wiki_dirt - ", root_wiki_dirt)
    try:
        point_from = root_wiki_dirt.index('с корнем <i>')
        point_to = root_wiki_dirt.index('- <')
        root_wiki = root_wiki_dirt[point_from + 12:point_to + 2]
#        print(root_wiki)
    except:
        return (f"Request {data_item_query} was nothing returned")
# source
    try:
        source_drt = item.find("span", class_="source")
        source = str(source_drt.text)[1:-1]
#        print(source)
    except:
        pass

#Словарь - Часть речи:[Слово]
    try:
#        print("Collect the dictionary")
        my_list = [
            'формы',
            'имена собственные',
            'фамилии',
            'топонимы',
            'существительные',
            'прилагательные',
            'глаголы',
            'причастия',
            'деепричастия',
            'предикативы',
            'наречия',
            'частицы',
            'вводные слова',
            'междометия',
            'местоимения',
            'числительные'
        ]

        dict = item.find("td", class_="block-body")
        word_dict = {}
        for blc_part_of_speech in dict.find_all("li"):
            words = []
#            print(blc_part_of_speech.span)
#             part_of_speech = str(blc_part_of_speech.span)[6:-8]
#             print (part_of_speech)
            ppart_of_speech = [span.text for span in blc_part_of_speech.find_all('span')]
#            print(ppart_of_speech)
            for i in range(len(ppart_of_speech)):
                for j in range(len(my_list)):
                    if my_list[j] in ppart_of_speech[i]:
                        part_of_speech = ppart_of_speech[i][0:-1]
            for link in blc_part_of_speech.find_all("a"):
                words.append(link.text)
            word_dict[part_of_speech] = words
#            print(word_dict)
    except:
        pass

# DataBase output
    for item in word_dict.items():
        part_of_speech = item[0]
#        print (item[0], item[1])
        for i in range(len(item[1])):
            pass
#            print (item[1][i], pattern_name, root, root_wiki, item[0])
            filling_words(item[1][i], pattern_name, root, root_wiki, item[0])


#Вывод в таблицу

    # data = {'Шаблон': pattern_name, 'Корень Wiktionary': root_wiki, 'Источник(если указан)': source,
    #         'Части речи и слова': [word_dict]}
    # print(data)
    # df = pd.DataFrame(data, index=[1])
    # pd.DataFrame(data, index=[1])
    # # df.to_csv("/Users/vladimirchi/Downloads/data.csv", index=False)
    # df.to_csv("data.csv", index=False)


# name = 'List_of_root_morphemes.txt'
#
# data_item_id = list
# with open(name, 'r', encoding='utf-8') as file:
#     data_item_id = file.readlines()
#     print(len(data_item_id), type(data_item_id))

#root = "прав"
#extractor("Шаблон:родств:прав")

# root = "акт"
# extractor("Шаблон:родств:акт")

dirt_str = "	да/да1/даж&дать	", "	Шаблон:родств:да#Шаблон:родств:да#Шаблон:родств:даж#Шаблон:родств:дать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	да/да1/даж&дать	", "	Шаблон:родств:да#Шаблон:родств:да#Шаблон:родств:даж#Шаблон:родств:дать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	дв/дв&два	", "	Шаблон:родств:дв#Шаблон:родств:дв#Шаблон:родств:два	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	двиг/дви/двиг/движ/двиз&двигать	", "	Шаблон:родств:двиг#Шаблон:родств:дви#Шаблон:родств:двиг#Шаблон:родств:движ#Шаблон:родств:двиз#Шаблон:родств:двигать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	де/де(j)/дё&деть;дело;надежда	", "	Шаблон:родств:де#Шаблон:родств:деj#Шаблон:родств:дё#Шаблон:родств:детьШаблон:родств:делоШаблон:родств:надежда	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	дел/дел&делить	", "	Шаблон:родств:дел#Шаблон:родств:дел#Шаблон:родств:делить	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	ден/ден/дён/дн1&день	", "	Шаблон:родств:ден#Шаблон:родств:ден#Шаблон:родств:дён#Шаблон:родств:дн#Шаблон:родств:день	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	др/дер/дёр/дерг/дёрг/дёрж/дир/дор/дорог3/др&дёргать	", "	Шаблон:родств:др#Шаблон:родств:дер#Шаблон:родств:дёр#Шаблон:родств:дерг#Шаблон:родств:дёрг#Шаблон:родств:дёрж#Шаблон:родств:дир#Шаблон:родств:дор#Шаблон:родств:дорог#Шаблон:родств:др#Шаблон:родств:дёргать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	держ/держ&держать	", "	Шаблон:родств:держ#Шаблон:родств:держ#Шаблон:родств:держать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	ед/е1/ед/ес2/я3/яд&еда	", "	Шаблон:родств:ед#Шаблон:родств:е#Шаблон:родств:ед#Шаблон:родств:ес#Шаблон:родств:я#Шаблон:родств:яд#Шаблон:родств:еда	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	езд-езж/езд/езж/ех&езда	", "	Шаблон:родств:езд-езж#Шаблон:родств:езд#Шаблон:родств:езж#Шаблон:родств:ех#Шаблон:родств:езда	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	жи/жи&жить	", "	Шаблон:родств:жи#Шаблон:родств:жи#Шаблон:родств:жить	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	зл/зл&зло	", "	Шаблон:родств:зл#Шаблон:родств:зл#Шаблон:родств:зло	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	игр/игор/игр/ыгр&игра	", "	Шаблон:родств:игр#Шаблон:родств:игор#Шаблон:родств:игр#Шаблон:родств:ыгр#Шаблон:родств:игра	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	каз/каж1/кажд1/каз1&казаться;сказать	", "	Шаблон:родств:каз#Шаблон:родств:каж#Шаблон:родств:кажд#Шаблон:родств:каз#Шаблон:родств:казатьсяШаблон:родств:сказать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	конец/кан/кон1&кончать	", "	Шаблон:родств:конец#Шаблон:родств:кан#Шаблон:родств:кон#Шаблон:родств:кончать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	корм/карм/корм1&кормить	", "	Шаблон:родств:корм#Шаблон:родств:карм#Шаблон:родств:корм#Шаблон:родств:кормить	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	кат/кат1/кач1&катать	", "	Шаблон:родств:кат#Шаблон:родств:кат#Шаблон:родств:кач#Шаблон:родств:катать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	лаг-лож/лаг/лег2/лёг2/леж/лёж/леч2/лог/лож1&лежать	", "	Шаблон:родств:лаг-лож#Шаблон:родств:лаг#Шаблон:родств:лег#Шаблон:родств:лёг#Шаблон:родств:леж#Шаблон:родств:лёж#Шаблон:родств:леч#Шаблон:родств:лог#Шаблон:родств:лож#Шаблон:родств:лежать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	лом/лам/лом&ломать	", "	Шаблон:родств:лом#Шаблон:родств:лам#Шаблон:родств:лом#Шаблон:родств:ломать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	люб/люб&любой;любить	", "	Шаблон:родств:люб#Шаблон:родств:люб#Шаблон:родств:любойШаблон:родств:любить	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	люд/люд	", "	Шаблон:родств:люд#Шаблон:родств:люд	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	один/один/одн	", "	Шаблон:родств:один#Шаблон:родств:один#Шаблон:родств:одн	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	пад/па1/пад/паж/пас1/пащ&падать	", "	Шаблон:родств:пад#Шаблон:родств:па#Шаблон:родств:пад#Шаблон:родств:паж#Шаблон:родств:пас#Шаблон:родств:пащ#Шаблон:родств:падать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	пи/па2/пи/по(j)1/пь&пить	", "	Шаблон:родств:пи#Шаблон:родств:па#Шаблон:родств:пи#Шаблон:родств:поj#Шаблон:родств:пь#Шаблон:родств:пить	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	пар/пар1&пар	", "	Шаблон:родств:пар#Шаблон:родств:пар#Шаблон:родств:пар	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	пах (пахать)/пах2/паш2&пахать	", "	Шаблон:родств:пах (пахать)#Шаблон:родств:пах#Шаблон:родств:паш#Шаблон:родств:пахать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	петь/пе/по3&петь	", "	Шаблон:родств:петь#Шаблон:родств:пе#Шаблон:родств:по#Шаблон:родств:петь	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	рв-рыв/рв/ров1/ры&рвать	", "	Шаблон:родств:рв-рыв#Шаблон:родств:рв#Шаблон:родств:ров#Шаблон:родств:ры#Шаблон:родств:рвать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	сад-саж/сад/саж/сажд/сед1/сёд/сес/сид/сиж1/сяд	", "	Шаблон:родств:сад-саж#Шаблон:родств:сад#Шаблон:родств:саж#Шаблон:родств:сажд#Шаблон:родств:сед#Шаблон:родств:сёд#Шаблон:родств:сес#Шаблон:родств:сид#Шаблон:родств:сиж#Шаблон:родств:сяд	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	сам/сам	", "	Шаблон:родств:сам#Шаблон:родств:сам	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	свет1/свес/свет/свеч/свещ	", "	Шаблон:родств:свет#Шаблон:родств:свес#Шаблон:родств:свет#Шаблон:родств:свеч#Шаблон:родств:свещ	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	серд/серд/серж/серч&сердце	", "	Шаблон:родств:серд#Шаблон:родств:серд#Шаблон:родств:серж#Шаблон:родств:серч#Шаблон:родств:сердце	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	сл/сл1/сол2/сыл&слать	", "	Шаблон:родств:сл#Шаблон:родств:сл#Шаблон:родств:сол#Шаблон:родств:сыл#Шаблон:родств:слать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	слаб/слаб&слабый	", "	Шаблон:родств:слаб#Шаблон:родств:слаб#Шаблон:родств:слабый	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	слад/слад/слажд/сласт/слащ/солаж/солод/солож/солощ&сладкий	", "	Шаблон:родств:слад#Шаблон:родств:слад#Шаблон:родств:слажд#Шаблон:родств:сласт#Шаблон:родств:слащ#Шаблон:родств:солаж#Шаблон:родств:солод#Шаблон:родств:солож#Шаблон:родств:солощ#Шаблон:родств:сладкий	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	смотр/сматр/смотр&смотреть	", "	Шаблон:родств:смотр#Шаблон:родств:сматр#Шаблон:родств:смотр#Шаблон:родств:смотреть	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	смех-смеш/сме1&смех	", "	Шаблон:родств:смех-смеш#Шаблон:родств:сме#Шаблон:родств:смех	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	снег/снег/снеж	", "	Шаблон:родств:снег#Шаблон:родств:снег#Шаблон:родств:снеж	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	сторон/сторон/стран&сторона	", "	Шаблон:родств:сторон#Шаблон:родств:сторон#Шаблон:родств:стран#Шаблон:родств:сторона	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	стро/стра/стро(j)&строить	", "	Шаблон:родств:стро#Шаблон:родств:стра#Шаблон:родств:строj#Шаблон:родств:строить	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	суд/суд1/суж/сужд&суд	", "	Шаблон:родств:суд#Шаблон:родств:суд#Шаблон:родств:суж#Шаблон:родств:сужд#Шаблон:родств:суд	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	суд1/суд2&судно	", "	Шаблон:родств:суд#Шаблон:родств:суд#Шаблон:родств:судно	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	тверд/тверд/твёрд/тверж/твержд&твёрдый	", "	Шаблон:родств:тверд#Шаблон:родств:тверд#Шаблон:родств:твёрд#Шаблон:родств:тверж#Шаблон:родств:твержд#Шаблон:родств:твёрдый	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	тем/тем2/тём/тм/тьм&темень	", "	Шаблон:родств:тем#Шаблон:родств:тем#Шаблон:родств:тём#Шаблон:родств:тм#Шаблон:родств:тьм#Шаблон:родств:темень	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	тер/тер1/тёр/тир/тор/тр2&тереть	", "	Шаблон:родств:тер#Шаблон:родств:тер#Шаблон:родств:тёр#Шаблон:родств:тир#Шаблон:родств:тор#Шаблон:родств:тр#Шаблон:родств:тереть	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	торг/торг1/торж1&торг	", "	Шаблон:родств:торг#Шаблон:родств:торг#Шаблон:родств:торж#Шаблон:родств:торг	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	тр/тр1&третий	", "	Шаблон:родств:тр#Шаблон:родств:тр#Шаблон:родств:третий	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	труд/труд/труж/тружд	", "	Шаблон:родств:труд#Шаблон:родств:труд#Шаблон:родств:труж#Шаблон:родств:тружд	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	туг/туг/туж&тугой	", "	Шаблон:родств:туг#Шаблон:родств:туг#Шаблон:родств:туж#Шаблон:родств:тугой	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	тя-тяг-тяж/тя/тяг/тяж/тяз&тянуть	", "	Шаблон:родств:тя-тяг-тяж#Шаблон:родств:тя#Шаблон:родств:тяг#Шаблон:родств:тяж#Шаблон:родств:тяз#Шаблон:родств:тянуть	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	у/у1&обуть	", "	Шаблон:родств:у#Шаблон:родств:у#Шаблон:родств:обуть	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	уголj/угл2/угол2&уголь	", "	Шаблон:родств:уголʲ#Шаблон:родств:угл#Шаблон:родств:угол#Шаблон:родств:уголь	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	узк/уж2/уз2&узкий	", "	Шаблон:родств:узк#Шаблон:родств:уж#Шаблон:родств:уз#Шаблон:родств:узкий	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	уч-ук/ук/уч&наука	", "	Шаблон:родств:уч-ук#Шаблон:родств:ук#Шаблон:родств:уч#Шаблон:родств:наука	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	ум/ум	", "	Шаблон:родств:ум#Шаблон:родств:ум	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	цвет/цве/цвес/цвет/цвеч	", "	Шаблон:родств:цвет#Шаблон:родств:цве#Шаблон:родств:цвес#Шаблон:родств:цвет#Шаблон:родств:цвеч	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	чит/ч3/чес2/чет/чёт/чит/чт&перечень;учесть	", "	Шаблон:родств:чит#Шаблон:родств:ч#Шаблон:родств:чес#Шаблон:родств:чет#Шаблон:родств:чёт#Шаблон:родств:чит#Шаблон:родств:чт#Шаблон:родств:переченьШаблон:родств:учесть	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	ше/ш/ше2/шед&дошлый;пошлина;шествие	", "	Шаблон:родств:ше#Шаблон:родств:ш#Шаблон:родств:ше#Шаблон:родств:шед#Шаблон:родств:дошлыйШаблон:родств:пошлинаШаблон:родств:шествие	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	шаг-шаж/шаг/шаж	", "	Шаблон:родств:шаг-шаж#Шаблон:родств:шаг#Шаблон:родств:шаж	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	ши/шв/шев/ши/шов&швея	", "	Шаблон:родств:ши#Шаблон:родств:шв#Шаблон:родств:шев#Шаблон:родств:ши#Шаблон:родств:шов#Шаблон:родств:швея	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
time.sleep(5)

dirt_str = "	шёпот/шеп/шёп&шептать	", "	Шаблон:родств:шёпот#Шаблон:родств:шеп#Шаблон:родств:шёп#Шаблон:родств:шептать	"
root = dirt_str[0].replace('\t', '')
query_str = dirt_str[1].replace('\t', '')
query_str_splt = query_str.split('#')
print(root, query_str_splt)
for i in range(len(query_str_splt)):
    extractor(query_str_splt[i])
