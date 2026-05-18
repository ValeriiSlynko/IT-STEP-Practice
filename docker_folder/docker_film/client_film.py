import requests

response = requests.get("http://localhost:8080/films")

print(response.json())
