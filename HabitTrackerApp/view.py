import sys
from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw

from new_user_view import NewUserDialog
from controller import get_users_controller, get_number_of_users_controller

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit tracker")
    
    def setup_ui(self):
        self.setFixedSize(500,500)
        self.app_layout = qtw.QGridLayout()
        self.test_button = qtw.QPushButton("Push me")
        self.app_layout.addWidget(self.test_button)
        self.main_window_widgets = qtw.QWidget()
        self.main_window_widgets.setLayout(self.app_layout)
        self.setCentralWidget(self.main_window_widgets)

    def setup_user_menu(self):
        user_menu = self.menuBar()
        set_user_menu = qtw.QMenu("&User", self)
        set_user_menu = self.add_users(set_user_menu)   
        register_new_user_action = qtw.QAction("&New user...", self)
        register_new_user_action.triggered.connect(self.create_new_user)
        set_user_menu.addAction(register_new_user_action)
        if set_user_menu != None:
            user_menu.addMenu(set_user_menu)
        self.setMenuBar(user_menu)

    def add_users(self, user_menu):
        users = get_users_controller()
        if len(users) > 0:
            for user in users:
                user_name = user["username"]
                user_action = qtw.QAction(f"&{user_name}", self)
                user_action.triggered.connect(lambda clicked, val=user_name: 
                                                    self.get_user_stats(val))
                user_menu.addAction(user_action)
            return user_menu
        else:   
            self.create_new_user()
        
    def create_new_user(self):
        new_user_window = NewUserDialog(self)
        if new_user_window.exec_() == 0 and get_number_of_users_controller() > 0:
            sys.exit()
             
    def get_user_stats(self, user_name):
        print(f"Getting user info for {user_name}")

app = qtw.QApplication([])
app_window = MainWindow()
app_window.setup_ui()
app_window.show()
app_window.setup_user_menu()
app.exec_()

