from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Gui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()

    def initUi(self):
        valueBeforeLabel = QLabel('Value before')
        valueAfterLabel = QLabel('Value after')
        fromCurrencyLabel = QLabel('From currency')
        toCurrencyLabel = QLabel('To currency')
        self.valueBefore = QLineEdit()
        self.valueAfter = QLineEdit()
        self.fromCurrency = QComboBox()
        self.toCurrency = QComboBox()
        self.convertButton = QPushButton('Convert')

        # Validator
        self.valueBefore.setValidator(QIntValidator())
        self.valueAfter.setValidator(QIntValidator())
        self.valueAfter.setReadOnly(True)

        # Layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(valueBeforeLabel, 1, 0)
        grid.addWidget(self.valueBefore, 1, 1)
        grid.addWidget(fromCurrencyLabel, 2, 0)
        grid.addWidget(self.fromCurrency, 2, 1)
        grid.addWidget(toCurrencyLabel, 3, 0)
        grid.addWidget(self.toCurrency, 3, 1)
        grid.addWidget(valueAfterLabel, 4, 0)
        grid.addWidget(self.valueAfter, 4, 1)
        grid.addWidget(self.convertButton, 5, 1)
        self.setLayout(grid)

        # Set up
        width, height = (400, 300)
        self.setWindowTitle("Currency converter")
        self.resize(width, height)

        # Center
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())