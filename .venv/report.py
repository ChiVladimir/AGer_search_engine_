from database import get_all, get_all_roots,get_words_from_roots
import io
from pprint import pprint

#print (get_all())
#exception = []
#outputs = get_all()
#name = 'words_all.txt'
#with open(name, 'a', encoding='utf-8') as file:
#    for output in outputs:
#        file.write(f'{output[0]}|{output[1]}|{output[2]}|{output[3]}|{output[4]}|{output[5]}\n')
#    file.close()

exception = []
outputs = get_all_roots()
#print (outputs)
name = 'roots_all.txt'
with open(name, 'a', encoding='utf-8') as file:
     for output in outputs:
#        print (output[0], output[1], output[2])
        words_returned = get_words_from_roots(output[1])
        words = [words_returned[i][0] for i in range(len(words_returned))]
        print (f'{output[0]}|{output[1]}|{output[2]}|{" ".join(words)}\n')
        file.write(f'{output[0]}|{output[1]}|{output[2]}|{" ".join(words)}\n')
     file.close()
