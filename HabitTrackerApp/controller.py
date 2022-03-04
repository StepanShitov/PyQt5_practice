import model

def get_users_controller():
    return(model.upload_users())

def create_new_user_controller(user_name):
    return (model.create_new_user(user_name))

def get_number_of_users_controller():
    return (model.get_number_of_users())

def get_user_progress_controller(user_name):
    return(model.get_user_progress(user_name))
