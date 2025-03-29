import requests

BASE = "http://127.0.0.1:5000/"

response = requests.get(BASE + "recommedation")



response2 = requests.get(BASE + "user")
response3 = requests.get(BASE + "user/<int:user_id>/bet")
response4 = requests.get(BASE + "user/<int:user_id>/recommendation")


print(response.json())

