from PyQt5 import QtWidgets as qtw
from PyQt5.QtCore import QRect, Qt, center
from PyQt5.QtWidgets import QApplication as qapp, QLabel, QLineEdit, QPushButton, QVBoxLayout

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setMainScreen()
        
        self.show()
    

    def setMainScreen(self):
        self.setWindowTitle("First app")
        self.setGeometry(100, 100, 200, 200)

        self.setLayout(QVBoxLayout())
        self.name_label = QLabel("Hey")
        self.name_label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(self.name_label)
        self.name_field = QLineEdit("Enter your name here")
        self.layout().addWidget(self.name_field)
        self.button = QPushButton("Say smth")
        self.layout().addWidget(self.button)   
        self.button.clicked.connect(self.test_function)

    def test_function(self):
        print("hello world")
        self.name_label.clear()
        self.name_label.setText("{}, {}".format(self.name_label.text(), self.name_field.text()))

app = qapp([])
mw = MainWindow()

app.exec_()