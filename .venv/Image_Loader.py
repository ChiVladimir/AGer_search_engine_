from fileinput import filename

from PIL import Image
from PIL import ImageDraw, ImageFont
import subprocess
import os
import requests
import urllib.request
from io import BytesIO
import urllib
from urllib.request import urlopen
import httplib2
import webbrowser



def resize_foto(name, multi):
    image = Image.open(name)
    w, h = image.size
    return image.resize((round(w * multi), round(h * multi)))

def paste_foto(base_image, foto_4_paste, position):
    base_image.paste(foto_4_paste, position, foto_4_paste)
#    base_image.show()
    return base_image

def text_insert(image_4_text, font, text, fill, position):
    fin_image = image_4_text.copy()
    draw = ImageDraw.Draw(fin_image)
    draw.text(position, text, fill, font)
    return fin_image

url = "https://disk.yandex.ru/d/sxrAZSaRWNl6gg/20bar.JPG"

data = requests.get(url).content

f = open('20bar.JPG','wb+') # Открываем новый файл

f.write(data) # Сохранение данных изображения в переменную data в файл

f.close() # Закрываем файл

#img = Image.open('20bar.JPG') # Открываем, смотрим
#img.show()

file_path = '20bar.JPG'

# Загрузка изображения
#urllib.request.urlretrieve(url, file_path)

# resource = urlopen(url)
# out = open(url, 'wb')
# out.write(resource.read())
# out.close()

# h = httplib2.Http('.cache')
# response, content = h.request(url)
# out = open(url, 'wb')
# out.write(content)
# out.close()

webbrowser.open(url)