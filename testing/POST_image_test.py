import requests

r = requests.post('http://127.0.0.1:8000', files={'file': open('test_image.png', 'rb')})

print(r.text)