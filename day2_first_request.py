import requests
import json

url = "https://api.github.com/users/torvalds"
response = requests.get(url)
data = response.json()

print(json.dumps(data, indent=2))


