import imp
from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw

from controller import get_users

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit tracker")
    
    def set_app_ui(self):
        self.resize(500,500)
        user_menu = self.menuBar()
        set_user_menu = qtw.QMenu("&User", self)
        set_user_menu = self.add_users(set_user_menu)     
        user_menu.addMenu(set_user_menu)
        self.setMenuBar(user_menu)

    def add_users(self, user_menu):
        for user in get_users():
            user_menu.addAction(f"&{user}")
        return user_menu


app = qtw.QApplication([])
app_window = MainWindow()
app_window.set_app_ui()
app_window.show()

app.exec_()