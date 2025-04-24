import requests
from API.key_api import header

API_URL = "https://staging.connectable.site/api/event/"

day = "25"
mounth = "04"
year = "2025"


data_create_event = {
    "client_id": "api",
    "color": "00d43f",
    "comment": 'Коммент API',
    'created': f'{year}-{mounth}-{day}T08:54:16.157Z',
    "creator": "67be00a0e6e983001ee2847c",
    "date": f"{year}-{mounth}-{day}T13:00:00+03:00",
    "duration": 60,
    "emailSend": False,
    "end": f"{year}-{mounth}-{day}T14:00:00+03:00",
    "grants": {
        "all": True,
        "all_heads": False,
        'depts': [],
        "empls": []
    },
    "lang": "ru",
    "name": "Тест API",
    "periodical": {
        "enabled": False,
    },
    "userEmail": "t2@gmail.com",
    "userId": "67be00a0e6e983001ee2847c",
    "utcOffset": 180,
    "zoom": "https://github.com/"
}

respponse_create_event = requests.post(API_URL, headers=header, json=data_create_event)

def test_create_event():
    assert respponse_create_event.status_code == 201
    print(f'код ответа:{respponse_create_event.status_code}')