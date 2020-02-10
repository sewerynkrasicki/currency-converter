from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys
from Gui import Gui
import requests


class Converter():
    def __init__(self):
        self.api_key = 'YOUR-API-KEY'
        self.gui = Gui()
        self.gui.show()
        self.getSymbols()
        self.gui.convertButton.clicked.connect(self.getComboBoxFrom)
        self.gui.convertButton.clicked.connect(self.getComboBoxTo)
        self.gui.convertButton.clicked.connect(self.getValueBefore)
        self.gui.convertButton.clicked.connect(self.convertVal)

    # Getting currency symbols from API
    def getSymbols(self):
        url = fr'https://free.currconv.com/api/v7/currencies?apiKey={self.api_key}'
        request = requests.get(url)
        result = request.json()
        resultList = list(result.items())
        resultDict = resultList[0][1]
        listOfSymbols = []
        for key in resultDict.keys():
            listOfSymbols.append(key)
        self.gui.fromCurrency.addItems(listOfSymbols)
        self.gui.toCurrency.addItems(listOfSymbols)

    def getComboBoxFrom(self):
        return self.gui.fromCurrency.currentText()

    def getComboBoxTo(self):
        return self.gui.toCurrency.currentText()

    def getValueBefore(self):
        return self.gui.valueBefore.text()

    def convertVal(self):
        cur1 = self.getComboBoxFrom()
        cur2 = self.getComboBoxTo()
        val = self.getValueBefore()
        url = fr'https://free.currconv.com/api/v7/convert?apiKey={self.api_key}&q={cur1}_{cur2}&compact=y'
        request = requests.get(url)
        result = request.json()
        resultList = list(result.items())
        resultDict = resultList[0][1].get('val')
        calculatedVal = float(val) * resultDict
        self.gui.valueAfter.setText(str(calculatedVal))


app = QApplication([])
converter = Converter()
sys.exit(app.exec_())
