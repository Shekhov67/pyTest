import requests
from API.key_api import header

for i in range(0, 3):

    if i == 0:
        type_group = 'ОТКРЫТОЙ'
    elif i == 1:
        type_group = 'ЗАКРЫТОЙ'
    elif i == 2:
        type_group = 'ПРИВАТНОЙ'


    API_URL = 'https://staging.connectable.site/api/group/'

    data_group = {
        'client_id': "api",
        'creator': "67be00a0e6e983001ee2847c",
        'creatorId': "67be00a0e6e983001ee2847c",
        'description': f"Описание {type_group} группы API",
        'emailSend': False,
        'lang': "ru",
        'name': f"Название {type_group} группы API",
        'type': f'{i}',
        'userEmail': "t2@gmail.com"
    }

    response_create_group = requests.post(API_URL, headers=header, json=data_group)

    def test_create_group():
        assert response_create_group.status_code == 201
        print(f'код ответа: {response_create_group.status_code}')