import requests, json


server_address = 'http://127.0.0.1:8000/get_picture/'
#server_address = 'http://46.101.109.17:8000/get_picture/'
#server_address = 'http://imdel.tk:8000/get_picture/'


r = requests.post(server_address, {'id' : '1'})
print(r.text)
