from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw

def create_new_user():
    class NewUserWindow(qtw.QMainWindow):
        def __init__(self):
            super().__init__()
            self.setWindowTitle("Create new user")
            self.setFixedSize(200,200)

    new_user_app = qtw.QApplication([])
    new_user_app_window = NewUserWindow()
    new_user_app_window.show()

    new_user_app.exec_()