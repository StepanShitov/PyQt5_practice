from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QRect, Qt, center
from PyQt5.QtWidgets import QApplication as qapp, QLabel, QLineEdit, QVBoxLayout

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First app")
        self.setGeometry(100, 100, 200, 200)
        self.setLayout(QVBoxLayout())
        name_label = QLabel("Hey")
        name_label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(name_label)
        name_field = QLineEdit("Enter your name here")
        self.layout().addWidget(name_field)
        self.show()

app = qapp([])
mw = MainWindow()

app.exec_()