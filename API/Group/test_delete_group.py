import requests
from API.key_api import header
from API.Group.group_list import group_id

API_URL = f'https://staging.connectable.site/api/group/{group_id}'
response_delete_group = requests.delete(API_URL, headers=header)


def test_group_delete():
    assert response_delete_group.status_code == 200
    print(f'код ответа: {response_delete_group.status_code}')


