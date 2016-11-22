import requests, json, os
from time import time
import traceback

data =  {
        'publisher' : 5,
        'text' : 'abc',
        'latitude' : '59.913869',
        'longitude' : '10.75225',
        }

headers = {'Authorization': 'Token 16b333307185048cecfbd76994aec125e91ffa11'}

filename = 'test_image.jpg'
temp_file_name = str(time()) + '.jpg'
os.rename(filename, temp_file_name)
files = {'image' : open(temp_file_name, 'rb')}

url = 'http://127.0.0.1:8000/publish_photo/'
#url = 'http://imdel.tk:8000/publish_photo/'

try:
    r = requests.post(url, files = files, data=data, headers=headers)
    print(r)
except:
    traceback.print_exc()
os.rename(temp_file_name, filename)


