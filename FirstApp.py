from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel, QWidget, QCheckBox, QVBoxLayout, QAction, QApplication, QLabel, QMainWindow, QMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        checkB = QCheckBox()
        checkB.setCheckState(Qt.Checked)
        layout.addWidget(checkB)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        label = QLabel("hey")
        layout.addWidget(label)

        print("Hello")


app = QApplication([])

window = MainWindow()
window.show()

app.exec()