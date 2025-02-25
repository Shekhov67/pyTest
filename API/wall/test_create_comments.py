import requests
from API.key_api import header


API_URL = 'https://staging.connectable.site/api/comment'

comment_data_feed = {
    'author': '67be00a0e6e983001ee2847c',
    'author_name': 'Админ Тестов',
    'client_id': 'api',
    'mentions': [],
    'message': 'Коммент API Лента событий',
    'owner': '67be00a0e6e983001ee2847c',
    'parent': {
        'type': 'post',
        'id': '67be00bfe6e983001ee2875a',
        'where': 'feed'
    }
}

response_create_comment_feed = requests.post(API_URL, headers=header, json=comment_data_feed)

def test_create_comment_feed():
    assert response_create_comment_feed.status_code == 201
    print(f'код ответа:{response_create_comment_feed.status_code}')


comment_data_company = {
    'author': '67be00a0e6e983001ee2847c',
    'author_name': 'Админ Тестов',
    'client_id': 'api',
    'mentions': [],
    'message': 'Коммент API Новости компании',
    'owner': '67be00a0e6e983001ee2847c',
    'parent': {
        'type': 'post',
        'id': '67be00c5e6e983001ee287f9',
        'where': 'company'
    }
}

response_create_comment_company = requests.post(API_URL, headers=header, json=comment_data_company)

def test_create_comment_company():
    assert response_create_comment_company.status_code == 201
    print(f'код ответа:{response_create_comment_company.status_code}')