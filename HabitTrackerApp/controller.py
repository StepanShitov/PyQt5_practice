from distutils.command.upload import upload
import model

def get_users():
    users = model.upload_users()
    if users == "File not found":
        return ["a", "b"]
    else:
        return users