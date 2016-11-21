import requests, json, os
from time import time
import traceback

data = 	{
		'text' : 'abc',
		'latitude' : '59.913869',
		'longitude' : '10.75225'
		}

filename = 'test_image.jpg'
temp_file_name = str(time()) + '.jpg'
os.rename(filename, temp_file_name)
files = {'image' : open(temp_file_name, 'rb')}

server_address = 'http://127.0.0.1:8000/publish_photo/'
#server_address = 'http://imdel.tk:8000/publish_photo/'


try:
	r = requests.post(server_address, files = files, data=data)
	print(r)
except:
	traceback.print_exc()
os.rename(temp_file_name, filename)


