import requests
from bs4 import BeautifulSoup
import socks
import socket
import re
from fake_useragent import UserAgent
#UserAgent().chrome



def checkIP():
    ip = requests.get('http://checkip.dyndns.org').content
    soup = BeautifulSoup(ip, 'html.parser')
    print(soup.find('body').text)

checkIP()

url_chld = 'https://www.avito.ru/4008831513'

response = requests.get(url_chld, headers={'User-Agent': UserAgent().chrome})

for key, value in response.request.headers.items():
    print(key+": "+value)

print(url_chld)
soup = BeautifulSoup(response.text, 'lxml')
print (soup)




# socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
# socket.socket = socks.socksocket
#
# print(socket)
#
# checkIP()