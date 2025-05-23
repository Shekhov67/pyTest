import requests
from API.key_api import header

body = {
    "name": "Тест 40",
    "text": "Например: Нам важно, ваше мнение. Помогите нам сделать компанию ещё лучше!",
    "questions": [
        {
            "_id": "68302cb018d34f75d5f088b2",
            "type": "LONG_TEXT",
            "text": "1",
            "required": True
        },
        {
            "_id": "68302cb0ae6b85c12086ee06",
            "type": "SHORT_TEXT",
            "text": "1"
        },
        {
            "_id": "68302cb1ee48fb228df4f51c",
            "type": "MANY_OF_LIST",
            "text": "1",
            "list": [
                {"_id": "68302cb6339cda2ea18d5613", "text": "Ответ 1"},
                {"_id": "68302e65bd70d1e8097588d6", "text": "Ответ 2"},
                {"_id": "68302e6a97313b7342b047c4", "text": "Ответ 3"},
                {"_id": "68302e6b81b88f7cf5fbe585", "text": "Ответ 4"},
                {"_id": "68302e6b81b88f7cf5fbe586", "text": "Ответ 5"},
                {"_id": "68302e6b81b88f7cf5fbe587", "text": "Ответ 6"},
                {"_id": "68302e6b81b88f7cf5fbe588", "text": "Ответ 7"},
                {"_id": "68302e6b81b88f7cf5fbe589", "text": "Ответ 8"},
                {"_id": "68302e6b81b88f7cf5fbe58a", "text": "Ответ 9"},
                {"_id": "68302e6b81b88f7cf5fbe58b", "text": "Ответ 10"},
                {"_id": "68302e6b81b88f7cf5fbe58c", "text": "Ответ 11"},
                {"_id": "68302e6b81b88f7cf5fbe58d", "text": "Ответ 12"},
                {"_id": "68302e6b81b88f7cf5fbe58e", "text": "Ответ 13"},
                {"_id": "68302e6b81b88f7cf5fbe58f", "text": "Ответ 14"},
                {"_id": "68302e6b81b88f7cf5fbe590", "text": "Ответ 15"},
                {"_id": "68302e6b81b88f7cf5fbe591", "text": "Ответ 16"},
                {"_id": "68302e6b81b88f7cf5fbe592", "text": "Ответ 17"},
                {"_id": "68302e6b81b88f7cf5fbe593", "text": "Ответ 18"},
                {"_id": "68302e6b81b88f7cf5fbe594", "text": "Ответ 19"},
                {"_id": "68302e6b81b88f7cf5fbe595", "text": "Ответ 20"},
                {"_id": "68302e6b81b88f7cf5fbe596", "text": "Ответ 21"},
                {"_id": "68302e6b81b88f7cf5fbe597", "text": "Ответ 22"},
                {"_id": "68302e6b81b88f7cf5fbe598", "text": "Ответ 23"},
                {"_id": "68302e6b81b88f7cf5fbe599", "text": "Ответ 24"},
                {"_id": "68302e6b81b88f7cf5fbe59a", "text": "Ответ 25"},
                {"_id": "68302e6b81b88f7cf5fbe59b", "text": "Ответ 26"},
                {"_id": "68302e6b81b88f7cf5fbe59c", "text": "Ответ 27"},
                {"_id": "68302e6b81b88f7cf5fbe59d", "text": "Ответ 28"},
                {"_id": "68302e6b81b88f7cf5fbe59e", "text": "Ответ 29"},
                {"_id": "68302e6b81b88f7cf5fbe59f", "text": "Ответ 30"},
                {"_id": "68302e6b81b88f7cf5fbe5a0", "text": "Ответ 31"},
                {"_id": "68302e6b81b88f7cf5fbe5a1", "text": "Ответ 32"},
                {"_id": "68302e6b81b88f7cf5fbe5a2", "text": "Ответ 33"},
                {"_id": "68302e6b81b88f7cf5fbe5a3", "text": "Ответ 34"},
                {"_id": "68302e6b81b88f7cf5fbe5a4", "text": "Ответ 35"},
                {"_id": "68302e6b81b88f7cf5fbe5a5", "text": "Ответ 36"},
                {"_id": "68302e6b81b88f7cf5fbe5a6", "text": "Ответ 37"},
                {"_id": "68302e6b81b88f7cf5fbe5a7", "text": "Ответ 38"},
                {"_id": "68302e6b81b88f7cf5fbe5a8", "text": "Ответ 39"},
                {"_id": "68302e6b81b88f7cf5fbe5a9", "text": "Ответ 40"}
            ]
        }
    ],
    "answers": [],
    "grants": {
        "all": True,
        "all_heads": False,
        "empls": [],
        "depts": []
    },
    "type": "opened",
    "recipients": [],
    "author": "682585ca0ac353001e5be714",
    "client_id": "an4",
    "created": "2025-05-23T08:14:46.582Z",
    "updated": "2025-05-23T08:14:46.582Z"
}
url = 'https://staging.connectable.site/api/poll'
response = requests.post(url, headers=header, json=body)

print(response.status_code)