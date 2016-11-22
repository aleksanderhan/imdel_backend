import requests, json, os
from time import time
import traceback

data =  {
        'publisher' : 1,
        'text' : 'abc',
        'latitude' : '59.913869',
        'longitude' : '10.75225',
        }

headers = {'Authorization': 'Token 05b759da3739aae07853e7210137eab34d100392'}

filename = 'test_image.jpg'
temp_file_name = str(time()) + '.jpg'
os.rename(filename, temp_file_name)
files = {'image' : open(temp_file_name, 'rb')}

url = 'http://127.0.0.1:8000/publish_photo/'
#url = 'http://imdel.tk:8000/publish_photo/'

try:
    r = requests.post(url, files = files, data=data, headers=headers)
    print(r.text)
except:
    traceback.print_exc()
os.rename(temp_file_name, filename)


