# import socket
#
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if len(data) < 1:
#         break
#     print(data.decode(),end='')
#
# mysock.close()
#
#
# import urllib.request, urllib.parse, urllib.error
# from bs4 import BeautifulSoup
# import ssl
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
#
# a = int(input("count-:"))
# b = int(input("position-:"))
#
# url = input('Enter - ')
# html = urllib.request.urlopen(url, context=ctx).read()
# soup = BeautifulSoup(html, 'html.parser')
#
#
#
# for _ in range(a):
#     c=b
#     tags = soup('a')
#     for tag in tags:
#         if (c==1):
#             break
#         c-=1
#     print(tag.get('href', None))
#     url = tag.get('href', None)
#     html = urllib.request.urlopen(url, context=ctx).read()
#     soup = BeautifulSoup(html, 'html.parser')
#

# import xml.etree.ElementTree as ET
# import urllib.request
# a=[]
# flag=0
# fhand = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_139637.xml')
# for line in fhand:
#     if flag!=0:
#         a.append(line.decode().strip())
#     flag+=1
# a="\n".join(a)
# tree = ET.fromstring(a)
# count=tree.findall('comments/comment')
# sum=0
# for i in count:
#     sum+=int(i.find('count').text)
#
# print(sum)

#
# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl
#
# api_key = False
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro
#
# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else:
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'
#
# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE
# flag = 0
# while flag == 0:
#     address = input('Enter location: ')
#     if len(address) < 1: break
#
#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)
#
#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')
#
#     try:
#         js = json.loads(data)
#     except:
#         js = None
#
#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue
#     flag += 1
# lng = js['results'][0]['place_id']
#
# print(lng)
#

class partyanimal:
    x=0
    def party(self):
        self.x=self.x+1
        print("so far x is",self.x)
a=partyanimal()
a.party()
a.party()
a.party()
print(type(a))