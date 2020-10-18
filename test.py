#!venv/bin/python3
import requests
import random
import string
import json
from requests.auth import HTTPBasicAuth


"""test create new user"""
base_url = 'http://127.0.0.1:5000/api/'

email = "".join(random.choice(string.ascii_lowercase) for i in range(8))
password = "".join(random.choice(string.ascii_lowercase) for i in range(8))
x = requests.post(base_url+'users', json={"email": email, "name":"test", "password":password, "lastname":"test", "telephone": 69696969})
print(json.loads(x.text))


"""test return user"""
y = requests.get(base_url+'users/'+str(json.loads(x.text)['id']))
print(json.loads(y.text))

"""test get token"""
z = requests.get(base_url+'token', auth=HTTPBasicAuth(email, password))
print(json.loads(z.text))
token = json.loads(z.text)['token']


"""test get ressource with token"""
w = requests.get(base_url+'resource', auth=HTTPBasicAuth(token, ''))
print(json.loads(w.text))