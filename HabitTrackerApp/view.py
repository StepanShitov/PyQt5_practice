import sys
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from new_user_view import NewUserDialog
from controller import get_users_controller, get_number_of_users_controller

class MainWindow(qtw.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Habit tracker")
    
    def setup_ui(self):
        self.setFixedSize(500,500)
        #Working on main window widgets location
        self.app_layout = qtw.QVBoxLayout()
        self.header_layout = qtw.QHBoxLayout()
        self.watch_and_spend_points_layout = qtw.QVBoxLayout()
        #Main window widgets:
        self.add_habit_btn = qtw.QPushButton("Add new habit")
        self.add_habit_btn.setFixedHeight(23)
        self.header_layout.addWidget(self.add_habit_btn)
        
        self.points_label = qtw.QLabel("Points")
        self.spend_points_btn = qtw.QPushButton("Get additional day-off")
        self.spend_points_btn.setFixedHeight(23)
        self.watch_and_spend_points_layout.addWidget(self.points_label)
        self.watch_and_spend_points_layout.addWidget(self.spend_points_btn)
        self.watch_and_spend_points_layout.setSpacing(20)

        
        self.header_layout.addLayout(self.watch_and_spend_points_layout)
        self.header_layout.setSpacing(round(self.width() / 3))

        self.app_layout.addLayout(self.header_layout)
        self.habits_progress = qtw.QTableView()
        self.delete_habit = qtw.QPushButton("Stop working on habit")
        self.delete_habit.setFixedSize(round(self.width() / 3), 23)
        self.app_layout.addWidget(self.habits_progress)
        self.app_layout.addWidget(self.delete_habit)


        self.main_window_widgets = qtw.QWidget()
        self.main_window_widgets.setLayout(self.app_layout)
        self.setCentralWidget(self.main_window_widgets)

    def setup_user_menu(self):
        self.user_menu = self.menuBar()
        self.set_user_menu = qtw.QMenu("&User", self)
        self.update_users_list()
        self.setMenuBar(self.user_menu)

    def add_users(self):
        users = get_users_controller()
        if len(users) > 0:
            for user in users:
                user_name = user["username"]
                user_action = qtw.QAction(f"&{user_name}", self)
                user_action.triggered.connect(lambda clicked, val=user_name: 
                                                    self.get_user_stats(val))
                self.set_user_menu.addAction(user_action)
            return self.set_user_menu
        else:   
            self.create_new_user()

    def update_users_list(self):
        self.set_user_menu = self.add_users()
        register_new_user_action = qtw.QAction("&New user...", self)
        register_new_user_action.triggered.connect(self.create_new_user)
        self.set_user_menu.addAction(register_new_user_action)
        if self.set_user_menu != None:
            self.user_menu.addMenu(self.set_user_menu)
        
    def create_new_user(self):
        new_user_window = NewUserDialog(self)
        if (new_user_window.exec_() == 0):
            if(get_number_of_users_controller() == 0):
                sys.exit()
            elif (get_number_of_users_controller() > 0):
                self.set_user_menu.clear()
                self.update_users_list()

    def get_user_stats(self, user_name):
        print(f"Getting user info for {user_name}")

app = qtw.QApplication([])
app_window = MainWindow()
app_window.setup_ui()
app_window.show()
app_window.setup_user_menu()
app.exec_()

