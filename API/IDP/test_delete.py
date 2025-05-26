import pytest
import requests
from API.key_api import header
from API.IDP.get_ipr import body_id


def test_delete_idp_valid_data():

    API_URL = f'https://staging.connectable.site/api/idp/{body_id}'

    response = requests.delete(API_URL, headers=header)
    assert response.status_code == 200

    print(f"Позитивный кейс: статус {response.status_code}, тело: {response.json()}")



