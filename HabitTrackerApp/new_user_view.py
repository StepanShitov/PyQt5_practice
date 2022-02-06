from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw

class NewUserDialog(qtw.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Adding new user")
        self.setFixedSize(250, 250)
        self.setup_ui()

    def setup_ui(self):
        self.app_layout = qtw.QVBoxLayout()
        self.name_label = qtw.QLabel("There are no registered users\n\nEnter your name here")
        self.name_input = qtw.QTextEdit()
        self.name_input.textChanged.connect(self.check_text_len)
        self.app_layout.addWidget(self.name_label)
        self.app_layout.addWidget(self.name_input)
        self.setLayout(self.app_layout)

    def check_text_len(self):
        user_input = self.name_input.toPlainText()
        if len(user_input) > 10:
            cursor = self.name_input.textCursor()
            cursor.movePosition(qtg.QTextCursor.End)
            self.name_input.setPlainText(user_input[:10])            
            self.name_input.setTextCursor(cursor)