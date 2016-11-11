import requests, json

POST = 	{
		'text' : 'lorem ipsum',
		'latitude' : '59.913869',
		'longitude' : '10.752245'
		}

r = requests.post(
	'http://127.0.0.1:8000/upload_image/', 
	files = {'image' : open('test_image.png', 'rb')}, data=POST)

#r = requests.post('http://127.0.0.1:8000/upload_image/', files = {'image' : open('test_image.png', 'rb')}, text='lorem ipsum', latitude='59.913869', longitude = '10.752245')

print(r.text)