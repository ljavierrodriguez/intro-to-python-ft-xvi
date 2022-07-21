import requests

response = requests.get('https://jsonplaceholder.typicode.com/users')

data = response.json()

for user in data:
    print(user['name'])

""" data = {
    "username": "",
    "password": ""
}

headers = {
    "Content-Type": 'application/json'
}

response = requests.post('', data=data, json=data, headers=headers) """