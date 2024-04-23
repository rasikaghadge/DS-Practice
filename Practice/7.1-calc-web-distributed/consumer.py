import requests

url = 'http://localhost:5000/hello'

response = requests.get(url)
data = response.json()

print(data['message'])