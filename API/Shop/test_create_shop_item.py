import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/shop/api/shop_items'

shop_item_data = {
    'amount': 100,
    'client_id': "api",
    'cost': 50,
    'description': "Описание товара",
    'name': "Худи-Шмуди"
}

response_create_item = requests.post(API_URL, headers=header, json=shop_item_data)

def test_create_shop_item():
    assert response_create_item.status_code == 200
    print(f'код ответа: {response_create_item.status_code}')