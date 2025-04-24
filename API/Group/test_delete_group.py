import requests
from API.key_api import header


def test_group_delete():
    API_URL = 'https://staging.connectable.site/api/group/byUser/67be00a0e6e983001ee2847c'
    response_list_group = requests.get(API_URL, headers=header)
    groups = response_list_group.json()
    print(groups)
    print(len(groups['result']))
    count_groups = len(groups['result'])
    for i in range(count_groups):
        group_id = groups['result'][i]['_id']
        print(group_id)
        API_URL = f'https://staging.connectable.site/api/group/{group_id}'
        response_delete_group = requests.delete(API_URL, headers=header)
        assert response_delete_group.status_code == 200
        print(f'код ответа: {response_delete_group.status_code}')



