import imp
import json

users = dict()

def upload_users():
    global users
    try:
        with open("users_info.json") as users_file:
            return((json.load(users_file))["users"])
    except OSError:
        return "File not found"

def create_new_user(user_name):
    if user_name not in users.keys(): users["username"] = user_name
    else: return ("user already exists")
    print(users)