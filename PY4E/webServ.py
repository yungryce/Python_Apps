# import xml.etree.ElementTree as ET

# input = '''
# <stuff>
#   <users>
#     <user x="2">
#       <id>001</id>
#       <name>Chuck</name>
#     </user>
#     <user x="7">
#       <id>009</id>
#       <name>Brent</name>
#     </user>
#   </users>
# </stuff>'''

# stuff = ET.fromstring(input)
# lst = stuff.findall('users/user')
# print('User count:', len(lst))

# for item in lst:
#     print('Name', item.find('name').text)
#     print('Id', item.find('id').text)
#     print('Attribute', item.get('x'))


# import json

# data = '''
# [
#   { "id" : "001",
#     "x" : "2",
#     "name" : "Chuck"
#   } ,
#   { "id" : "009",
#     "x" : "7",
#     "name" : "Brent"
#   }
# ]'''

# info = json.loads(data)
# print('User count:', len(info))

# for item in info:
#     print('Name', item['name'])
#     print('Id', item['id'])
#     print('Attribute', item['x'])




# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl

# api_key = 'AIzaSyCSe7MYr500aqqh-7jb5if2xW6Wq4N4tcc'
# # If you have a Google Places API key, enter it here
# # api_key = 'AIzaSy___IDByT70'
# # https://developers.google.com/maps/documentation/geocoding/intro

# if api_key is False:
#     api_key = 42
#     serviceurl = 'http://py4e-data.dr-chuck.net/json?'
# else :
#     serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# while True:
#     address = input('Enter location: ')
#     if len(address) < 1: break

#     parms = dict()
#     parms['address'] = address
#     if api_key is not False: parms['key'] = api_key
#     url = serviceurl + urllib.parse.urlencode(parms)

#     print('Retrieving', url)
#     uh = urllib.request.urlopen(url, context=ctx)
#     data = uh.read().decode()
#     print('Retrieved', len(data), 'characters')

#     try:
#         js = json.loads(data)
#     except:
#         js = None

#     if not js or 'status' not in js or js['status'] != 'OK':
#         print('==== Failure To Retrieve ====')
#         print(data)
#         continue

#     print(json.dumps(js, indent=4))

#     lat = js['results'][0]['geometry']['location']['lat']
#     lng = js['results'][0]['geometry']['location']['lng']
#     print('lat', lat, 'lng', lng)
#     location = js['results'][0]['formatted_address']
#     print(location)


# import urllib.request, urllib.parse, urllib.error
# import xml.etree.ElementTree as ET
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter Url:')
# data = urllib.request.urlopen(url, context=ctx).read()
# print("Retrieved", len(data), "characters")

# tree = ET.fromstring(data)
# counts = tree.findall('comments/comment')
# print("count:", len(counts))
# count = 0

# for item in counts:
#     item = int(item.find('count').text)
#     count += item
# print('Sum:', count)



# import urllib.request, urllib.parse, urllib.error
# import json
# import ssl

# # Ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

# url = 'http://py4e-data.dr-chuck.net/comments_1629404.json'
# data = urllib.request.urlopen(url, context=ctx).read()
# print('Retrieved', len(data), 'characters')

# info = json.loads(data)
# print('User count:', len(info))

# count = 0
# # print(info['comments'][0]['name'])
# for item in info['comments']:
#     a = int(item['count'])
#     count += a
# print('Sum', count)



import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = 42
# if api_key is False:
    # api_key = 42
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('::::')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    # data = urllib.request.urlopen(url).read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue
    place_id = js["results"][0]["place_id"]
    print(place_id)