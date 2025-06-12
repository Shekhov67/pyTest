import requests
from API.key_api import header



API_URL = 'https://staging.connectable.site/api/idp/list/682585ca0ac353001e5be714'

response = requests.get(API_URL, headers=header)

body = response.json()
print(body)

if body == {'result': []}:
    print('Нет ИПР')
else:
    body_id = body['result'][0]['_id']

    print(body_id)

# Выводим все _id из элементов result
# for item in data["result"]:
#     if "_id" in item:
#         print(item["_id"])