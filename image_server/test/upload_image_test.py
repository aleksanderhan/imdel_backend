import requests, json, os
from time import time

POST = 	{
		'imageText' : '',
		'latitude' : '59.913869',
		'longitude' : '10.75225'
		}

#server_address = 'http://127.0.0.1:8000/upload_image/'
server_address = 'http://46.101.109.17:8000/upload_image/'
#server_address = 'http://imdel.tk:8000/upload_image/'

filename = 'test_image.jpg'
temp_file_name = str(time()) + '.jpg'
os.rename(filename, temp_file_name)
r = requests.post(server_address, files = {'image' : open(temp_file_name, 'rb')}, data=POST)
os.rename(temp_file_name, filename)

print(r.text)
