import model

def get_users_controller():
    users = model.upload_users()
    if type(users) == str or len(users) == 0:
        return []
    else:
        return users

def create_new_user_controller(user_name):
    return (model.create_new_user(user_name))

def get_number_of_users_controller():
    return (model.get_number_of_users())

def setup_user_workspace_controller(user_name):
    pass
