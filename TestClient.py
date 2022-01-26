import requests

req = requests.post('http://127.0.0.1:5000/connect/Kirill')

print(req)

req = requests.get('http://127.0.0.1:5000/info')
