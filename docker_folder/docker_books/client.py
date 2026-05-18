import requests

response = requests.get("http://localhost:8080/books")

print(response.json())
