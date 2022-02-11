import imp
import json

users = dict()

def upload_users():
    try:
        with open("users_info1.json") as users_file:
            return((json.load(users_file))["users"])
    except OSError:
        return "File not found"

def create_new_user(user_name):
    users = upload_users()
    if users != "File not found":
        if user_name not in users.values(): 
            users["username"] = user_name
            return("")
        else: return("user already exists")
    else:
        with open("users_info1.json", mode="w") as output:
            json_new_line = json.dumps({"users": [{ "username": user_name }]})
            print(json_new_line, file=output)
            return("")

def get_number_of_users():
    return len(users)