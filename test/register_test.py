import requests

url = 'http://127.0.0.1:8000/register/'
#url = 'http://imdel.tk:8000/register/'

data = {'username':'testuser2', 'password':'testpassword2'}

r = requests.post(url, data=data)
print(r.text)