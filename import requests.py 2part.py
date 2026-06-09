import requests

# Exercise 1: Fetch user with ID 5 and print their phone number
print("=== Exercise 1 ===")

url = "https://jsonplaceholder.typicode.com/users/5"
response = requests.get(url)

data = response.json()

print("Phone Number:", data["phone"])


# Exercise 2: Check if a resource exists before printing data
print("\n=== Exercise 2 ===")

url = "https://jsonplaceholder.typicode.com/users/5"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Resource not found!")


# Exercise 3: Count how many comments are on post ID 1
print("\n=== Exercise 3 ===")

url = "https://jsonplaceholder.typicode.com/posts/1/comments"
response = requests.get(url)

comments = response.json()

print("Number of comments:", len(comments))