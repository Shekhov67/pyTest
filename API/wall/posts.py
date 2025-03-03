import requests
from API.key_api import header

# получение списка постов
posts_company = "https://staging.connectable.site/api/post/news/api/0"
posts_feed = 'https://staging.connectable.site/api/post/user_feed/67be00a0e6e983001ee2847c/0'

response_posts = requests.get(posts_company, headers=header)

#Получаем списк в json формате и проверяем наличие постов
list_data = response_posts.json()
print(list_data['result'][0]['_id'])
count_posts = len(list_data['result'])
print(count_posts)

for i in range(count_posts - 1):
    num_post_company = 0
    print(list_data['result'][num_post_company]['_id'])
    API_URL_POSTS = f"https://staging.connectable.site/post/{list_data['result'][num_post_company]['_id']}"
    print(API_URL_POSTS)
    posts_company_id = list_data['result'][num_post_company]['_id']

response_posts = requests.get(posts_feed, headers=header)

#Получаем списк в json формате и проверяем наличие постов
list_data = response_posts.json()
print(list_data['result'][0]['_id'])
count_posts = len(list_data['result'])
print(count_posts)

for i in range(count_posts - 1):
    num_post_feed = 0
    print(list_data['result'][num_post_feed]['_id'])
    API_URL_POSTS = f"https://staging.connectable.site/post/{list_data['result'][num_post_feed]['_id']}"
    print(API_URL_POSTS)
    posts_feed_id = list_data['result'][num_post_feed]['_id']