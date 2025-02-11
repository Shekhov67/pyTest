import requests

headers = {
    "Authorization": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXN1bHQiOnsiX2lkIjoiNjUxM2Q5ZDk1NGI3YmQwMDFlMTMxMGQ3IiwiY2xpZW50X2lkIjoidGVzdGluZzMiLCJlbWFpbCI6InQyQGdtYWlsLmNvbSIsImZpcnN0TmFtZSI6ItCh0L7RgtGA0YPQtNC90LjQuiIsImxhc3ROYW1lIjoi0JDQtNC80LjQvTEiLCJwaWNzIjpbeyJfaWQiOiI2NTEzZDlkOTU0YjdiZDAwMWUxMzEwZDciLCJzcmMiOiJodHRwczovL2Nvbm5lY3RhYmxlLnNpdGUvcHVibGljL3Rlc3RpbmczLzc1ZWViNDk3LTc1ZTgtNGIxNi05YWY0LWMzMjgxNWFmZWNmZC5qcGciLCJtaW5pIjoiaHR0cHM6Ly9jb25uZWN0YWJsZS5zaXRlL3B1YmxpYy90ZXN0aW5nMy83NWVlYjQ5Ny03NWU4LTRiMTYtOWFmNC1jMzI4MTVhZmVjZmQuanBnIn1dLCJpc1N1cGVyQWRtaW4iOmZhbHNlfSwiaWF0IjoxNzM5MjE0MzE1LCJleHAiOjE3NDE4OTI3MTV9.gnNaGk7ZX02Awaql-9s8RYGahU2gMqTTEazUiOTLeNU"
}
url = 'https://ors.connectable.site/api/poll/67a9b6dfd73113001e472720/excel?uid=67250e0ff16536001e36d91d'
response = requests.get(url, headers=headers)

print(response)

response = requests.get(url, headers=headers, stream=True)

with open('down.zip', 'wb') as file:
    for chunk in response.iter_content(chunk_size=8192):
        file.write(chunk)



