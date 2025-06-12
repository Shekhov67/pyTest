import requests
from API.key_api import header
from API.IDP.get_ipr import body_id


API_URL = 'https://staging.connectable.site/api/idp/683434f1b758ef001e457302/excel'

def test_load():
    #Выгрузка в Excel ИПР
    API_URL = f'https://staging.connectable.site/api/idp/{body_id}/excel'
    load_excel_response = requests.get(API_URL, headers=header)
    assert load_excel_response.status_code == 200
    print(f'Выгрузка ИПР в Excel файл успешна')

