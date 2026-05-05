import requests

url = "https://api.github.com/users/torvalds"
response = requests.get(url)
data = response.json()

print("Name:", data["name"])
print("Public repos:", data["public_repos"])
print("Followers:", data["followers"])
print("Location:", data["location"])
print("Bio:", data["bio"])
print("Created at:", data["created_at"])
