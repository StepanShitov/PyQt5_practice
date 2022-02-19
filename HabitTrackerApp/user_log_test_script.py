import json

with open("ivanov_logs.json") as user:
    text = json.load(user)

print(text["habits"])