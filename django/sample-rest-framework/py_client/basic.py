import requests

# endpoint = 'https://httpbin.org'
# endpoint = 'https://httpbin.org/anything'
endpoint = 'http://localhost:9000/api/'

# get_response = requests.get(endpoint)
get_response = requests.get(endpoint, params={'abc':123})
# get_response = requests.get(endpoint, data={'john':'hello world!'})

# print(get_response.text)
print(get_response.status_code)
# print(get_response.json()['message'])
print(get_response.json())


#  /anything returns a web/rest api in json while a non api returns html


