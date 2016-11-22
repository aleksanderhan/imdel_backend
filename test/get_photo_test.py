import requests, json

url = 'http://127.0.0.1:8000/get_photo/1'
#url = 'http://imdel.tk:8000/get_photo/1'

headers = {'Authorization': 'Token 46fd1c6b84c7eb3fefeb449c417854387718ce08'}

r = requests.get(url, headers=headers)
print(r)
