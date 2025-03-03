import requests
from API.key_api import header

# получение списка событий для пользаввтеля
events = "https://staging.connectable.site/api/user/api/events/access_for/67be00a0e6e983001ee2847c"

response_list_events = requests.get(events, headers=header)

print(response_list_events.json())

#Получаем списк в json формате и проверяем наличие событий
list_data = response_list_events.json()
print(list_data['result'][0]['_id'])
count_events = len(list_data['result'])

def test_delete_event():
# Проходим по всем событиям и удаляем
    for i in range(count_events - 1):
        #print(list_data['result'][i]['_id'])
        API_URL = f"https://staging.connectable.site/api/event/{list_data['result'][i]['_id']}"
        response_delete_events = requests.delete(API_URL, headers=header)
        assert response_delete_events.status_code == 200
        print(f'код ответа:{response_delete_events.status_code}')
