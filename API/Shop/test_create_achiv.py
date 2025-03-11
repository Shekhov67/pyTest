import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/shop/api/achievements'

achiv_data = {
    'client_id': "api",
    'description': "Описание достжениия",
    'label': "Название достижения",
    'name': "API"
}

response_create_achiv = requests.post(API_URL, headers=header, json=achiv_data)

def test_create_achiv():
    assert response_create_achiv.status_code == 200
    print(f'код ответа: {response_create_achiv.status_code}')
