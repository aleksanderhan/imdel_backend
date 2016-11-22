import requests, json

url = 'http://127.0.0.1:8000/get_thumbnails/'
#url = 'http://imdel.tk:8000/get_thumbnails/'

r = requests.post(url, {'latitude' : '59.913869', 'longitude' : '10.75225', 'radius' : '10', 'amount' : '3', 'offset' : '0'})
print(r.text)
