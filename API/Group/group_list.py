import requests
from API.key_api import header



API_URL = 'https://staging.connectable.site/api/group/byUser/67be00a0e6e983001ee2847c'

response_list_group = requests.get(API_URL, headers=header)

groups = response_list_group.json()

group_id = groups['result'][0]['_id']

print(group_id)





