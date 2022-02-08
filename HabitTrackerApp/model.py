import imp
import json

users = dict()

def upload_users():
    global users
    try:
        with open("users_info.json") as users_file:
            users = (json.load(users_file))["users"]
            return users
    except OSError:
        return "File not found"

def create_new_user(user_name):
    print(users)