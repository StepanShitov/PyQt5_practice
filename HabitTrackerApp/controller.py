import model

def get_users_controller():
    users = model.upload_users()
    if users == "File not found" or len(users) == 0:
        return []
    else:
        return users

def create_new_user_controller(user_name):
    model.create_new_user(user_name)