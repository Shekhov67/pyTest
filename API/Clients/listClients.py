import requests
from requests.auth import HTTPBasicAuth

token = ('eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyZXN1bHQiOnsiX2lkIjoiNjQ2MzY2YjlmNDFjZmIwMDFkNjU'
         'zYzZmIiwiZW1haWwiOiJ0MkBnbWFpbC5jb20iLCJmaXJzdE5hbWUiOiLQktCw0LTQuNC8IiwibGFzdE5hbWUiOiLQ'
         'kNC00LzQuNC90L7QsiIsInBpY3MiOlt7Il9pZCI6IjY0ZmYyOTBlZTQ4ODI1MDAxZTI5OWI5OSIsInNyYyI6Imh0dH'
         'BzOi8vc3RhZ2luZy5jb25uZWN0YWJsZS5zaXRlL3B1YmxpYy90ZXN0aW5nMy_QktCw0LTQuNC8INCQ0LTQvNC40L3Qv'
         'tCyX2F2YXRhcl9mdWxsLnBuZyIsIm1pbmkiOiJodHRwczovL3N0YWdpbmcuY29ubmVjdGFibGUuc2l0ZS9wdWJsaWMv'
         'dGVzdGluZzMv0JLQsNC00LjQvCDQkNC00LzQuNC90L7Qsl9hdmF0YXIucG5nIn1dLCJnb29nbGVJbWFnZSI6IiJ9LCJ'
         'pYXQiOjE3MTA2ODI4NTUsImV4cCI6MTcxMzM2MTI1NX0.8hKSTS2eWgCdYKTfSgev5N0SlJB4f7MLinhQz8T3TQU')

resp = (requests.get('https://staging.connectable.site/api/clients/by_ws/testing9',
    headers={'Authorization': token}).
        json())

print(resp)