import requests
from API.key_api import header

# URL API для лайка
API_URL = 'https://staging.connectable.site/api/post/like'

# Данные для запроса
like_data = {
    "emoji": "✊",
    "id": "67b731b43116aa001f23d25c",
    "like_type": "post",
    "post_id": "67b731b43116aa001f23d25c",
    "user_id": "65cf0c75f13f2f001e02f0f9",
    "where": "company"
}

# Выполнение POST-запроса
response_like = requests.post(API_URL, headers=header, json=like_data)

def test_like():
    # Проверка статуса ответа
    assert response_like.status_code == 200
    print(f'код ответа:{response_like.status_code}')

response_dislike = requests.post(API_URL, headers=header, json=like_data)

def test_dislike():
    assert response_dislike.status_code == 200
    print(f'код ответа:{response_dislike.status_code}')