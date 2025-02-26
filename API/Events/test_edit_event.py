import requests
from API.key_api import header
from API.Events.events import API_URL_EVENT

#API_URL = "https://staging.connectable.site/api/event/67bf2c1f05350f001e24c942"

day = "28"
mounth = "02"
year = "2025"


data_create_event = {
    "client_id": "api",
    "color": "#ff0000",
    "comment": 'Коммент API редактирование',
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
        "empls": {
            "0": {
                "id": "67be00a0e6e983001ee2847c",
                "mode": "r",
            }
        }
    },
    "lang": "ru",
    "name": "Тест API редактирование",
    "periodical": {
        "enabled": False,
    },
    "userEmail": "t2@gmail.com",
    "userId": "67be00a0e6e983001ee2847c",
    "utcOffset": 180
}

respponse_create_event = requests.put(API_URL_EVENT, headers=header, json=data_create_event)

def test_create_event():
    assert respponse_create_event.status_code == 200
    print(f'код ответа:{respponse_create_event.status_code}')