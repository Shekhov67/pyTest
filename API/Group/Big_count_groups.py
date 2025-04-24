import requests
from API.key_api import header
import asyncio

API_URL = 'https://staging.connectable.site/api/group/'

data = {
    'client_id': "api",
    'creator': "67be00a0e6e983001ee2847c",
    'creatorId': "67be00a0e6e983001ee2847c",
    'description': f"Описание  группы API",
    'emailSend': False,
    'lang': "ru",
    'name': f"Название  группы API",
    'type': f'1',
    'userEmail': "t2@gmail.com"
}
async def main():
    for i in range(100):
        response1 = requests.post(API_URL, headers=header, json=data)
        response2 = requests.post(API_URL, headers=header, json=data)
        response3 = requests.post(API_URL, headers=header, json=data)
        response4 = requests.post(API_URL, headers=header, json=data)
        response5 = requests.post(API_URL, headers=header, json=data)
        response6 = requests.post(API_URL, headers=header, json=data)
        response7 = requests.post(API_URL, headers=header, json=data)
        response8 = requests.post(API_URL, headers=header, json=data)
        response9 = requests.post(API_URL, headers=header, json=data)
        response10 = requests.post(API_URL, headers=header, json=data)
        response11 = requests.post(API_URL, headers=header, json=data)
        response12 = requests.post(API_URL, headers=header, json=data)
        response13 = requests.post(API_URL, headers=header, json=data)
        response14 = requests.post(API_URL, headers=header, json=data)
        response15 = requests.post(API_URL, headers=header, json=data)
        response16 = requests.post(API_URL, headers=header, json=data)
        response17 = requests.post(API_URL, headers=header, json=data)
        response18 = requests.post(API_URL, headers=header, json=data)
        response19 = requests.post(API_URL, headers=header, json=data)
        response20 = requests.post(API_URL, headers=header, json=data)

        print(response20.status_code)

asyncio.run(main())