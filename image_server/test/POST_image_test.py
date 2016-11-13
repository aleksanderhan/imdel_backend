import requests, json

POST = 	{
		'text' : 'lorem ipsum',
		'latitude' : '59.913869',
		'longitude' : '10.752245'
		}

server_adress = 'http://127.0.0.1:8000/upload_image'
#server_adress = 'http://46.101.109.17:8000/upload_image/'
#server_adress = 'http://imdel.tk:8000/upload_image/'


r = requests.post(server_adress, files = {'image' : open('test_image.jpg', 'rb')}, data=POST)

print(r.text)
