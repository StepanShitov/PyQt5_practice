import imp
import json

users = dict()

def upload_users():
    global users
    try:
        with open("users_info.json") as users_file:
            users = json.load(users_file)
            return users
    except OSError:
        return "File not found"