from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw

from controller import get_users

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit tracker")
    
    def setup_ui(self):
        self.setFixedSize(500,500)
        user_menu = self.menuBar()
        set_user_menu = qtw.QMenu("&User", self)
        set_user_menu = self.add_users(set_user_menu)     
        user_menu.addMenu(set_user_menu)
        self.setMenuBar(user_menu)

    def add_users(self, user_menu):
        for user in get_users(self):
            print(user)
            user_menu.addAction("&{}".format(user["username"]))
        return user_menu


app = qtw.QApplication([])
app_window = MainWindow()
app_window.setup_ui()
app_window.show()

app.exec_()