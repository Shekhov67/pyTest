import requests
from API.key_api import header

def dow_clients(id, cod):

    id_client = id
    code_client = cod

    # ПОДКЛЮЧЕН ПРОД!
    API_URL = f'https://connectable.site/api/clients/export/{id_client}'

    response = requests.get(API_URL, headers=header)

    assert response.status_code == 200
    print('Клиент выгружен', response.status_code)

    # Определяем путь для сохранения файла
    file_path = f"{code_client}.zip"

    # Сохраняем содержимое ответа в файл
    with open(file_path, 'wb') as file:
        file.write(response.content)

    print(f'Файл сохранён: {file_path}')

dow_clients('6513d95a54b7bd001e131037', 'testing3')