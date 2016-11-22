import requests, json

url = 'http://127.0.0.1:8000/get_photo/1'
#url = 'http://imdel.tk:8000/get_photo/1'

r = requests.get(url)
print(r)
