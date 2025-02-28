import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/shop/accrue'

body_accured = {
    'achievement': None,
    'amount': 10,
    'client_id': "api",
    'shop_manager': "67be00a0e6e983001ee2847c",
    'user': "67bee01ae6e983001ee963af",
    'users': {}
}

response_add_coins_user = requests.post(API_URL, headers=header, json=body_accured)

def test_add_coins_user():
    assert response_add_coins_user.status_code == 200
    print(f'код ответа:{response_add_coins_user.status_code}')