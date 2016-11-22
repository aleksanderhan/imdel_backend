import requests, json

url = 'http://127.0.0.1:8000/fetch_thumbnails/'
#url = 'http://imdel.tk:8000/fetch_thumbnails/'

data = {'latitude' : '59.913869', 'longitude' : '10.75225', 'radius' : '10', 'amount' : '3', 'offset' : '0'}
headers = {'Authorization': 'Token 16b333307185048cecfbd76994aec125e91ffa11'}

r = requests.post(url, data=data, headers=headers)
print(r.text)
