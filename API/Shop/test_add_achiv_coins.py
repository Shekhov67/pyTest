import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/shop/accrue'

body_accured = {
    'achievement': '67c1828596946f001e96a5be',
    'amount': 100,
    'client_id': "api",
    'shop_manager': "67be00a0e6e983001ee2847c",
    'user': "67bee01ae6e983001ee963af",
    'users': {}
}

response_add_achiv_coins = requests.post(API_URL, headers=header, json=body_accured)

def test_add_achiv_coins_user():
    assert response_add_achiv_coins.status_code == 200
    print(f'код ответа:{response_add_achiv_coins.status_code}')