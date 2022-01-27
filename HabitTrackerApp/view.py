import imp
from PyQt5 import QtWidgets as qtw
from PyQt5.QtWidgets import QMenuBar
import PyQt5.QtGui

from controller import Hello

def set_app_window():
    global app_window
    app_menu = app_window.menu
    app_window.setMenuBar(app_menu)
    

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

app = qtw.QApplication([])
app_window = MainWindow()
set_app_window()
app_window.show()

app.exec_()