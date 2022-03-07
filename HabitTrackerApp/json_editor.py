from collections import UserList
import json

def get_users():
    try:
        with open("users_info.json") as users_file:
            try:
                data = json.load(users_file) 
                return(data["users"])
            except json.decoder.JSONDecodeError:
                return("File is empty")
    except OSError:
        return("File not found")

def add_new_user(user_name, users):
    if type(users) != str:
        for user in users:
            print(user["username"])
            if user["username"] == user_name:
                return("User already exists")
        users.append({'username': user_name})
        with open("users_info.json", mode="w") as output:
            print("{\"users\":\n" + 
                    json.dumps(users).replace("}, {", "},\n\t{") + "\n}", 
                    file=output)
        return("")
    else:
        with open("users_info.json", mode="w") as output:
            json_new_line = json.dumps({"users": [{ "username": user_name }]})
            print(json_new_line, file=output)
            return("")

def setup_workspace(user_name):
    #current_added field is for completed week, if false - we need to +1 point and change to true
    initial_info = {"points":{"balance": 5, "previous_added": True}, 
                    "habits": {}}
    initial_user_activity = json.dumps(initial_info, indent=1, sort_keys=True)
    with open(f"users_logs/{user_name}_logs.json", "w") as new_user_log:
        print(initial_user_activity, file=new_user_log)
    return("")
