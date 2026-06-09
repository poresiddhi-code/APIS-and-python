import requests

url = "https://jsonplaceholder.typicode.com/users/5"

response = requests.get(url)

data = response.json()

print("Phone:", data["phone"])