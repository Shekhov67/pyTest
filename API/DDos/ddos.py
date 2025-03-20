import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/loginPage'

data = {
    'email': "t2@gmail.com",
    'lang': "ru",
    'login': "",
    'password': "111111",
    'workspace': "ttu"
}

for i in range(10):
    response = requests.post(API_URL, headers=header, json=data)
    print(response.status_code)