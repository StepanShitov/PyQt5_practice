from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw

from new_user_view import NewUserDialog
from controller import get_users

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit tracker")
    
    def setup_ui(self):
        self.setFixedSize(500,500)
        self.app_layout = qtw.QGridLayout()
        self.test_button = qtw.QPushButton("Push me")
        self.test_button.clicked.connect(self.test)
        self.app_layout.addWidget(self.test_button)
        self.main_window_widgets = qtw.QWidget()
        self.main_window_widgets.setLayout(self.app_layout)
        self.setCentralWidget(self.main_window_widgets)

    def test(self, s):
        print("hey")

    def setup_user_menu(self):
        user_menu = self.menuBar()
        set_user_menu = qtw.QMenu("&User", self)
        set_user_menu = self.add_users(set_user_menu)   
        if set_user_menu != None:
            user_menu.addMenu(set_user_menu)
            self.setMenuBar(user_menu)

    def add_users(self, user_menu):
        users = get_users()
        print(len(users))
        if len(users) > 0:
            for user in users:
                print(user)
                user_action = qtw.QAction("&{}".format(user["username"]))
                user_action.triggered.connect(self.get_user_stats)
                user_menu.addAction("&{}".format(user["username"]))
            return user_menu
        else:
            self.create_new_user()
        
    def create_new_user(self):
        new_user_window = NewUserDialog(self)
        new_user_window.exec_()

    # def get_user_stats(self, e):

app = qtw.QApplication([])
app_window = MainWindow()
app_window.setup_ui()
app_window.show()
app_window.setup_user_menu()

app.exec_()