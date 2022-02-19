import json_editor

def upload_users():
    return json_editor.get_users()

def create_new_user(user_name):
    existing_users = upload_users()
    status = json_editor.add_new_user(user_name, existing_users)
    status = json_editor.setup_workspace(user_name)
    return(status)
    

def get_number_of_users():
    return len(upload_users())