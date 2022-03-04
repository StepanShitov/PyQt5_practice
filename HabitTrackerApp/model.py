import json

import json_editor

def upload_users():
    users = json_editor.get_users()
    if type(users) == str or len(users) == 0:
        return []
    else:
        return users

def create_new_user(user_name):
    existing_users = upload_users()
    status = json_editor.add_new_user(user_name, existing_users)
    status = json_editor.setup_workspace(user_name)
    return(status)
        

def get_number_of_users():
    return len(upload_users())

def get_user_progress(username):
    with open(f"users_logs/{username}_logs.json") as user_data:
        try:
            data = json.load(user_data) 
            print(data)
        except json.decoder.JSONDecodeError:
            return("File is empty")