from database import get_all, get_all_roots,get_words_from_roots
import io
from pprint import pprint
import unicodedata

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

def replace_characters(original, new, str):
    for i in range(len(original) - 1):
        str = str.replace(original[i], new[i])
    return str

def delete_accent(word):
    char_preserve = ["й", "ё", "Ё"] #буквы, несправедливо попавшие под убивание диакритических знаков
    placeholders = ["@", "#", "%"]  #знаки, на которые мы будем их менять
    temp = replace_characters(char_preserve, placeholders, word)
    temp = remove_accents(temp)
    res = replace_characters(placeholders, char_preserve, temp)
    return res

def root_cleaning(root):
    hook_1 = root.find("/")
    hook_2 = root.find("&")

    return f'@{root[(hook_1 + 1):hook_2]}$'

#print (get_all())
exception = []
outputs = get_all()
name = 'words_all.txt'
with open(name, 'a', encoding='utf-8') as file:
   for output in outputs:
       word_acc_del = delete_accent(output[1])
       clean_root = root_cleaning(output[2])
       file.write(f'{word_acc_del}|{clean_root}|{output[3]}|{output[5]}\n')
   file.close()

exception = []
outputs = get_all_roots()
#print (outputs)
name = 'roots_all.txt'
with open(name, 'a', encoding='utf-8') as file:
     for output in outputs:
        clean_root = root_cleaning(output[0])
        words_returned = get_words_from_roots(output[1])
        words = [words_returned[i][0] for i in range(len(words_returned))]
#        print (f'{output[0]}|{output[1]}|{output[2]}|{" ".join(words)}\n')
        file.write(f'{clean_root}|{output[1]}|{output[2]}|{" ".join(words)}\n')
     file.close()
