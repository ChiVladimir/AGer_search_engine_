from database import get_word_and_root



def word_extract(line): # экстрагируем из строки слово и проверяем наличие @...$
    flag = True # Слово, необработанное ранее - нет @...$
    word = line[0:(line.find("#"))]
    if line.find("@") >= 0 and line.find("#") >= 0:
        flag = False
    return word, flag

def word_check(word, flag): # проверяем слово в базе, возвращаем корень, в базе ставим отметку
    root = get_word_and_root(word, flag)
    return root

def root_cleaning(root):
    if len(root) > 0:
        hook_1 = root.find("/")
        hook_2 = root.find("&")

        return f'@{root[(hook_1 + 1):hook_2]}$'
    else:
        return ''

def line_update(line, root): #склеиваем строку
    name = 'ks_013_updated.txt'
    with open(name, 'a', encoding='utf-8') as file:
#        print(f'{line}{root_cleaning(root)}')
#        line_into = f'{line}{root_cleaning(root)}'
        file.write(f'{line[:-1]}{root_cleaning(root)}\n')
        file.close()


# line = "аэропоезд#аэроп`оезд#аэроп`оезд, -а, мн. -`а, -`ов"
#
# word, flag = word_extract(line)
# print(word, flag)
# root = word_check(word, flag)
# line_update(line, root)

name = 'ks_013.txt'

with open(name, 'r', encoding='utf-8') as file:
    for line in file:
        try:
            word, flag = word_extract(line)
#           print(word, flag)
            root = word_check(word, flag)
            line_update(line, root)
        except:
            line_update(line, '')
            print ("Error line for request", line)