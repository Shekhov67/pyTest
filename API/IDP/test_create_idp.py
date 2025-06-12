import requests
from API.key_api import header

API_URL = 'https://staging.connectable.site/api/idp'

#Валидные данные
def test_create_idp_valid_data():
    body = {
        "client_id": "an4",
        "title": "Valid Test",
        "creator": "682585ca0ac353001e5be714",
        "employee": "682ec044aea362001e1c937a",
        "observer": "682c369aa724fb001e4529aa",
        "description": "Позитивный тест"
    }
    response = requests.post(API_URL, headers=header, json=body)
    assert response.status_code == 201
    print(f"Позитивный кейс: статус {response.status_code}, тело: {response.json()}")

#Отсутствует заголовок
def test_create_idp_missing_title():
    body = {
        "client_id": "an4",
        "creator": "682585ca0ac353001e5be714",
        "employee": "682ec044aea362001e1c937a",
        "observer": "682c369aa724fb001e4529aa",
        "description": "Без заголовка"
    }
    response = requests.post(API_URL, headers=header, json=body)
    assert response.status_code == 400 or response.status_code == 422
    print(f"Отсутствует title: статус {response.status_code}, тело: {response.text}")

#Поле creator с невалидным ID
def test_create_idp_invalid_creator():
    body = {
        "client_id": "an4",
        "title": "Invalid Creator",
        "creator": "invalid_id",
        "employee": "682ec044aea362001e1c937a",
        "observer": "682c369aa724fb001e4529aa",
        "description": "creator невалиден"
    }
    response = requests.post(API_URL, headers=header, json=body)
    assert response.status_code in [400, 422, 500]
    print(f"Невалидный creator: статус {response.status_code}, тело: {response.text}")

#Отправка пустого тела запроса
def test_create_idp_empty_body():
    response = requests.post(API_URL, headers=header, json={})
    assert response.status_code in [400, 422, 500]
    print(f"Пустое тело: статус {response.status_code}, тело: {response.text}")

#Неизвестный client_id
def test_create_idp_unknown_client_id():
    body = {
        "client_id": "fdsfdfsd1234",
        "title": "Неизвестный client_id",
        "creator": "682585ca0ac353001e5be714",
        "employee": "682ec044aea362001e1c937a",
        "observer": "682c369aa724fb001e4529aa",
        "description": "Тест с неизвестным client_id"
    }
    response = requests.post(API_URL, headers=header, json=body)
    assert response.status_code in [400, 404, 500, 502]
    print(f"Неизвестный client_id: статус {response.status_code}, тело: {response.text}")
