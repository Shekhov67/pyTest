import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/post'

data_post_feed = {
    "attachment": [],
    "author": {
        "client_id": "api",
        "deletion_mark": False,
        "email": "t2@gmail.com",
        "files": [],
        "firstName": "Админ",
        "followers": [],
        "followersEmail": [],
        "fullName": "Админ >> Тестов",
        "fullShortName": "Тестов А.",
        "gender": "man",
        "hrm": {
            "gender": "man"
        },
        "id": "67be00a0e6e983001ee2847c",
        "lang": "ru",
        "lastName": "Тестов",
        "middleName": "",
        "online": "true",
        "pics": [],
        "positions": [""],
        "roles": ["wall", "address", "groups", "structures", "calendar", "vacancies", "knowl_base", "services",
                  "adaptation", "ideas", "no_silent", "polls", "chat", "shop", "task_tracker", "vacations", "dark_theme", "admin"],
        "_id": "67be00a0e6e983001ee2847c",
    },
    "author_ref": "67be00a0e6e983001ee2847c",
    "client_id": "api",
    "emailSend": False,
    "extFormat": False,
    "for": [],
    "formData": None,
    "isGreeting": False,
    "lang": "ru",
    "mentions": [],
    "message": "Тест API пост",
    "parent": {
        "id": 0,
        "type": "feed",
    }
}


data_post_company = {
    "attachment": [],
    "author": {
        "client_id": "api",
        "deletion_mark": False,
        "email": "t2@gmail.com",
        "files": [],
        "firstName": "Админ",
        "followers": [],
        "followersEmail": [],
        "fullName": "Админ >> Тестов",
        "fullShortName": "Тестов А.",
        "gender": "man",
        "hrm": {
            "gender": "man"
        },
        "id": "67be00a0e6e983001ee2847c",
        "lang": "ru",
        "lastName": "Тестов",
        "middleName": "",
        "online": "true",
        "pics": [],
        "positions": [""],
        "roles": ["wall", "address", "groups", "structures", "calendar", "vacancies", "knowl_base", "services",
                  "adaptation", "ideas", "no_silent", "polls", "chat", "shop", "task_tracker", "vacations", "dark_theme", "admin"],
        "_id": "67be00a0e6e983001ee2847c",
    },
    "author_ref": "67be00a0e6e983001ee2847c",
    "client_id": "api",
    "emailSend": False,
    "extFormat": False,
    "for": [],
    "formData": None,
    "isGreeting": False,
    "lang": "ru",
    "mentions": [],
    "message": "Тест API пост",
    "parent": {
        "id": 0,
        "type": "company",
    }
}

def test_create_post_feed():
    response_create_post = requests.post(API_URL, headers=header, json=data_post_feed)
    assert response_create_post.status_code == 201
    print(f'код ответа:{response_create_post.status_code}')

def test_create_post_company():
    response_create_post = requests.post(API_URL, headers=header, json=data_post_company)
    assert response_create_post.status_code == 201
    print(f'код ответа:{response_create_post.status_code}')