from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from controller import create_new_user_controller

class TextEdit(qtw.QTextEdit):
    def keyPressEvent(self, event):
        super().keyPressEvent(event)
        if event.key() >= 16777219 and event.key() <= 16777221:
            self.enter_press_handler()
    
    def enter_press_handler(self):
        user_input = self.toPlainText().split("\n")
        cursor = self.textCursor()
        cursor.movePosition(qtg.QTextCursor.End)
        self.setPlainText(user_input[0])            
        self.setTextCursor(cursor)

class NewUserDialog(qtw.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Adding new user")
        self.setFixedWidth(250)
        self.setup_ui()

    def setup_ui(self):
        self.app_layout = qtw.QVBoxLayout()
        self.app_layout.setSpacing(10)
        self.name_label = qtw.QLabel("""There are no registered users
                                        \nEnter your name here
                                        \n (max lenth 10)""")
        
        self.name_input = TextEdit()
        self.name_input.setFixedHeight(30)
        self.name_input.setWordWrapMode(qtg.QTextOption.NoWrap)
        self.name_input.textChanged.connect(self.check_user_input)
        self.name_input.setFocus()

        self.create_new_user_btn = qtw.QPushButton("Create user")
        self.create_new_user_btn.clicked.connect(self.add_new_user)

        self.app_layout.addWidget(self.name_label)
        self.app_layout.addWidget(self.name_input)
        self.app_layout.addWidget(self.create_new_user_btn)
        self.setLayout(self.app_layout)

    def check_user_input(self):
        user_input = self.name_input.toPlainText()
        if len(user_input) > 10:
            cursor = self.name_input.textCursor()
            cursor.movePosition(qtg.QTextCursor.End)
            self.name_input.setPlainText(user_input[:10])            
            self.name_input.setTextCursor(cursor)
    
    def add_new_user(self):
        user_name = self.name_input.toPlainText()
        if len(user_name) > 0:
            if len(create_new_user_controller(user_name)) > 0:
                self.show_error_dialog("User already exists")
            else:
                self.close()
        else:
            self.show_error_dialog("Name field is empty")
    
    def show_error_dialog(self, message):
        empty_name_msg = qtw.QMessageBox(self)
        empty_name_msg.setWindowTitle("Warning")
        empty_name_msg.setText(message)
        empty_name_msg.setIcon(qtw.QMessageBox.Warning)
        empty_name_msg.setStandardButtons(qtw.QMessageBox.Retry)
        empty_name_msg.exec_()
    
    