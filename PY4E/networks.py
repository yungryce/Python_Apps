# import socket

# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)

# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')

# mysock.close()


# import socket
# import time

# HOST = 'data.pr4e.org'
# PORT = 80
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect((HOST, PORT))
# mysock.sendall(b'GET http://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
# count = 0
# picture = b""

# while True:
#     data = mysock.recv(5120)
#     if len(data) < 1: break
#     #time.sleep(0.25)
#     count = count + len(data)
#     print(len(data), count)
#     picture = picture + data

# mysock.close()

# # Look for the end of the header (2 CRLF)
# pos = picture.find(b"\r\n\r\n")
# print('Header length', pos)
# print(picture[:pos].decode())

# # Skip past the header and save the picture data
# picture = picture[pos+4:]
# fhand = open("stuff.jpg", "wb")
# fhand.write(picture)
# fhand.close()


# import urllib.request, urllib.parse, urllib.error

# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

# counts = dict()
# for line in fhand:
#     words = line.decode().split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1
# print(counts)


# import urllib.request, urllib.parse, urllib.error

# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg').read()
# fhand = open('cover3.jpg', 'wb')
# fhand.write(img)
# fhand.close()

# import urllib.request, urllib.parse, urllib.error

# img = urllib.request.urlopen('http://data.pr4e.org/cover3.jpg')
# fhand = open('cover3.jpg', 'wb')
# size = 0
# while True:
#     info = img.read(100000)
#     if len(info) < 1: break
#     size = size + len(info)
#     fhand.write(info)

# print(size, 'characters copied.')
# fhand.close()


# import urllib.request, urllib.parse, urllib.error
# import re
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# links = re.findall(b'href="(http[s]?://.*?)"', html)
# for link in links:
#     print(link.decode())


import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
print(html)
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
# for tag in tags:
    # print(tag.get('href', None))