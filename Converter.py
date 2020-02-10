from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Gui import Gui


class Converter():
    def __init__(self):
        pass






app = QApplication([])
gui = Gui()
gui.show()
sys.exit(app.exec_())
