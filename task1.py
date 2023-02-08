import requests

data = {"task": 3, "result": "abggafgfgafgfgafgfg"}

response = requests.post("https://nodus.caseguru.ru/trainee/tasks", json=data)
print(response.text)