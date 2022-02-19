import json

def get_users():
    try:
        with open("users_info.json") as users_file:
            return((json.load(users_file))["users"])
    except OSError:
        return "File not found"

def add_new_user(user_name, users):
    if users != "File not found":
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
    
    return("")
