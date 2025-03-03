import requests
from API.key_api import header
from API.wall.posts import posts_company_id, posts_feed_id


# URL API для лайка
API_URL = 'https://staging.connectable.site/api/post/like'

# Данные для запроса лайка в ленте событий
like_data_feed_post = {
    "emoji": "❤️",
    "id": f"{posts_feed_id}",
    "like_type": "post",
    "post_id": f"{posts_feed_id}",
    "user_id": "67be00a0e6e983001ee2847c",
    "where": "feed"
}

# Выполнение POST-запроса
response_like_feed_post = requests.post(API_URL, headers=header, json=like_data_feed_post)

def test_like_feed_post():
    # Проверка статуса ответа
    assert response_like_feed_post.status_code == 200
    print(f'код ответа:{response_like_feed_post.status_code}')

# Данные для запроса лайка в новостной ленте
like_data_company_post = {
    "emoji": "💪",
    "id": f"{posts_company_id}",
    "like_type": "post",
    "post_id": f"{posts_company_id}",
    "user_id": "67be00a0e6e983001ee2847c",
    "where": "company"
}

response_like_company_post = requests.post(API_URL, headers=header, json=like_data_company_post)


def test_like_company_post():
    assert response_like_company_post.status_code == 200
    print(f'код ответа:{response_like_company_post.status_code}')