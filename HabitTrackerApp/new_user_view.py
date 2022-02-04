from PyQt5 import QtGui
from PyQt5 import QtWidgets as qtw

class NewUserDialog(qtw.QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Adding new user")
        self.setFixedSize(250, 250)
        self.setup_ui()

    def setup_ui(self):
        app_layout = qtw. QVBoxLayout()
        name_label = qtw.QLabel("Enter your name here")
        name_input = qtw.QTextEdit()
        app_layout.addWidget(name_label)
