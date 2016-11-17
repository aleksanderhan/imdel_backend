import requests, json


server_address = 'http://127.0.0.1:8000/get_thumbnails/'
#server_address = 'http://46.101.109.17:8000/get_thumbnails/'
#server_address = 'http://imdel.tk:8000/get_thumbnails/'


r = requests.post(server_address, {'latitude' : '59.913869', 'longitude' : '10.75225', 'radius' : '10', 'amount' : '3', 'offset' : '0'})
print(r.text)
