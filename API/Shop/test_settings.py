import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/shop'

data_settings_shop = {
    'client_id': "api",
    'coin': 'коины',
    'coin_code': 'con',
    'managers': ["67be00a0e6e983001ee2847c"],
    'name': 'АПИШНЫЙ',
    '__v': 0,
    '_id': "67c160fac1279b2d32212bbf"
}

response_setting_shop = requests.put(API_URL, headers=header, json=data_settings_shop)

def test_setting_shop():
    assert response_setting_shop.status_code == 200
    print(f'код ответа: {response_setting_shop.status_code}')