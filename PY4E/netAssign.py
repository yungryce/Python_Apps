# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = b'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, "html.parser")

# tags = soup('span')
# count = 0
# for tag in tags:
#     numbers = int(tag.contents[0])
#     count += int(numbers)
# print(count)


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

count = int(input('Enter number of times:'))
pos = int(input('Enter Position:'))
i = 0
lst = list()
url = input('URL:')

while i < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')

    for tag in tags:
        site  = tag.get('href', None)
        lst.append(site)
    url = lst[pos - 1]
    lst = []
    i += 1
name = re.findall('.+by_([A-Za-z]+)', url)
print(name)