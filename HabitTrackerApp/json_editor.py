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
    initial_info = {"points":[{"balance": 0}, {"current_added": "true"}], 
                    "habits": []}
    initial_user_activity = json.dumps(initial_info)
    print(type(initial_user_activity))
    # with open(f"{user_name}_logs.json", "w") as new_user_log:
    #     print())

    # print(initial_user_activity)
    return("")
