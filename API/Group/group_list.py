import requests
from API.key_api import header



API_URL = 'https://staging.connectable.site/api/group/byUser/67be00a0e6e983001ee2847c'

response_list_group = requests.get(API_URL, headers=header)

groups = response_list_group.json()
#print(groups)
print(len(groups['result']))
count_groups = len(groups['result'])

for i in range(count_groups):
    group_id = groups['result'][i]['_id']
    print(group_id)





