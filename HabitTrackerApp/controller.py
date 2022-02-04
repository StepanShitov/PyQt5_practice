from distutils.command.upload import upload
import model
import new_user_view

def get_users():
    users = model.upload_users()
    print(users)
    if users == "File not found" or len(users) == 0:
        return []
    else:
        return users