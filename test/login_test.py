import requests

url = 'http://127.0.0.1:8000/login/'
#url = 'http://imdel.tk:8000/login/'

r = requests.post(url, data={'username':'testuser2', 'password':'testpassword2'})
print r.text