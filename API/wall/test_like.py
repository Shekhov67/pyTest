import requests

header = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXN1bHQiOnsiX2"
                     "lkIjoiNjVjZjBjNzVmMTNmMmYwMDFlMDJmMGY5IiwiY2xpZW50X2lkIjoidGVzdGluZzkiLCJlbWFpbCI6InQyQ"
                     "GdtYWlsLmNvbSIsImZpcnN0TmFtZSI6ItCQ0LTQvNC40L0iLCJsYXN0TmFtZSI6ItCS0LDQtNC40LwiLCJwaWNzIjpbeyJ"
                     "faWQiOiI2N2IxZjFlYjYxNTg0YjAwMWUxYThlMzIiLCJzcmMiOiJodHRwczovL3N0YWdpbmcuY29ubmVjdGFibGUuc2l0ZS9wdWJsaWMvdG"
                     "VzdGluZzkvNzFmZTc0NTYtZDMzNC00MmJkLTk4ZTAtMWI1YzgwMjZhYjU3LmdpZiIsIm1pbmkiOiJodHRwczovL3N0YWdpbmcuY29ubmVjdGFib"
                     "GUuc2l0ZS9wdWJsaWMvdGVzdGluZzkvYzZkZWRmNjYtZjgyMi00N2MwLTlhMWMtZDJiODQwYWIwZjNhLmdpZiJ9XSwiaXNTdXBlckFkbWluIjpmYWxzZX0"
                     "sImlhdCI6MTc0MDQxOTk2MywiZXhwIjoxNzQzMDk4MzYzfQ.f25rDYT8NF_UVTy6KETM5qevkkFNHkoHcaZslbM-GDk"
}

# URL API для лайка
API_URL = 'https://staging.connectable.site/api/post/like'

# Данные для запроса
like_data = {
    "emoji": "✊",
    "id": "67b731b43116aa001f23d25c",
    "like_type": "post",
    "post_id": "67b731b43116aa001f23d25c",
    "user_id": "65cf0c75f13f2f001e02f0f9",
    "where": "company"
}

# Выполнение POST-запроса
response = requests.post(API_URL, headers=header, json=like_data)

# Проверка статуса ответа
if response.status_code == 200:
    print("Лайк успешно поставлен!")
    print("Ответ сервера:", response.json())  # Вывод тела ответа (если есть)
else:
    print(f"Ошибка: {response.status_code}")
    print("Сообщение об ошибке:", response.text)  # Вывод сообщения об ошибке