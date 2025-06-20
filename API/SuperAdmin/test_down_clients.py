import requests
from API.key_api import header

def test_dow_clients():

    i = '67a063e938f437001f200f0e'
    code_client = ('test')

    API_URL = f'https://staging.connectable.site/api/clients/export/{i}'

    response = requests.get(API_URL, headers=header)

    assert response.status_code == 200
    print('Клиент выгружен')

    # Определяем путь для сохранения файла
    file_path = f"{code_client}.zip"

    # Сохраняем содержимое ответа в файл
    with open(file_path, 'wb') as file:
        file.write(response.content)

    print(f'Файл сохранён: {file_path}')