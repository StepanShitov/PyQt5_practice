from distutils.command.upload import upload
import model
import new_user_view

def get_users(main_window):
    users = model.upload_users()
    if users == "File not found" or len(users) == 0:
        new_user_view.create_new_user()
        return ["a", "b"]
    else:
        return users