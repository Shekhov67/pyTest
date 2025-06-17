import requests
from API.key_api import header
from TestSuites.smoke.test_module import url
def test_create_and_delete_idp():
    API_URL = f'{url}api/idp'

    # Тело запроса на создание ИПР
    body = {
        "client_id": "an4",
        "title": "Test Create+Delete",
        "creator": "682585ca0ac353001e5be714",
        "employee": "682ec044aea362001e1c937a",
        "observer": "682c369aa724fb001e4529aa",
        "description": "ИПР, созданный для удаления"
    }
    response = requests.post(API_URL, headers=header, json=body)
    assert response.status_code == 201
    print(f"Создание ИПР: статус {response.status_code}")
    #Получаем id созданного ИПР
    API_URL = 'https://staging.connectable.site/api/idp/list/682585ca0ac353001e5be714'

    response = requests.get(API_URL, headers=header)

    body = response.json()
    body_id = body['result'][0]['_id']
    assert body_id is not None, "Не удалось получить ID созданного ИПР"

    print(f"Создан ИПР: {body_id}")

    # Удаление созданного ИПР
    delete_url = f'https://staging.connectable.site/api/idp/{body_id}'
    delete_response = requests.delete(delete_url, headers=header)
    print(delete_response.status_code)

    assert delete_response.status_code == 200
    print(f"Удаление успешно: статус {delete_response.status_code}")