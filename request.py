import requests
import json
data = '{"url":"https://www.facebook.com/abc.exe"}'
print(type(json.loads(data)))
a = requests.post('http://127.0.0.1:8000/api/m/checkurls/', data=data,headers={'Content-type': 'application/json'})
print(a.text)