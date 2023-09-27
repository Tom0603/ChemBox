import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QGridLayout, QWidget, QPushButton, \
    QLineEdit, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem


class ChemBox(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.left = 100
        self.top = 0
        self.width = 1920
        self.height = 1080
        self.title = "ChemBox"
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tabBar = TabBar()
        self.setCentralWidget(self.tabBar)

        self.idealGasLaw = IdealGasLaw()
        self.tabBar.tab1.setLayout(self.idealGasLaw.idealGasLayout)

        self.chemBalancer = ChemBalancer()
        self.tabBar.tab3.setLayout(self.chemBalancer.balancerLayout)

        # self.interactiveTable = InteractiveTable()
        # self.tabBar.tab2.setLayout(self.interactiveTable.tableLayout)


class IdealGasLaw(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.idealGasLayout = QGridLayout()

        # Initialise Ideal Gas Law (IGL) properties
        self.idealGasConstant = 8.314

        self.pressureInputIGL = QLineEdit()
        self.volumeInputIGL = QLineEdit()
        self.temperatureInputIGL = QLineEdit()
        self.molesInputIGL = QLineEdit()

        self.pressureLabelIGL = QLabel("Pressure:")
        self.volumeLabelIGL = QLabel("Volume:")
        self.temperatureLabelIGL = QLabel("Temperature:")
        self.molesLabelIGL = QLabel("Amount of substance - moles:")
        self.calculateButtonIGL = QPushButton('Calculate')
        self.resultLabelIGL = QLabel('Result will appear here')

        self.pressureConversions = {
            "Pa": 1.0,
            "kPa": 1000.0,
        }

        self.temperatureConversions = {
            "°C": 273.15,
            "°K": 0.0,
        }

        self.volumeConversions = {
            "cm³": 0.000001,
            "dm³": 0.001,
            "m³": 1.0,

        }

        self.pressureDropDownIGL = QComboBox()
        self.volumeDropDownIGL = QComboBox()
        self.temperatureDropDownIGL = QComboBox()

        self.idealGasLayout.addWidget(self.pressureLabelIGL, 0, 0)
        self.idealGasLayout.addWidget(self.pressureInputIGL, 0, 1)
        self.idealGasLayout.addWidget(self.pressureDropDownIGL, 0, 2)

        self.idealGasLayout.addWidget(self.volumeLabelIGL, 1, 0)
        self.idealGasLayout.addWidget(self.volumeInputIGL, 1, 1)
        self.idealGasLayout.addWidget(self.volumeDropDownIGL, 1, 2)

        self.idealGasLayout.addWidget(self.temperatureLabelIGL, 2, 0)
        self.idealGasLayout.addWidget(self.temperatureInputIGL, 2, 1)
        self.idealGasLayout.addWidget(self.temperatureDropDownIGL, 2, 2)

        self.idealGasLayout.addWidget(self.molesLabelIGL, 3, 0)
        self.idealGasLayout.addWidget(self.molesInputIGL, 3, 1)
        self.idealGasLayout.addWidget(self.calculateButtonIGL, 4, 0)
        self.idealGasLayout.addWidget(self.resultLabelIGL, 4, 1)

        self.pressureDropDownIGL.addItem("Pa")
        self.pressureDropDownIGL.addItem("kPa")

        self.volumeDropDownIGL.addItem("cm³")
        self.volumeDropDownIGL.addItem("dm³")
        self.volumeDropDownIGL.addItem("m³")

        self.temperatureDropDownIGL.addItem("°C")
        self.temperatureDropDownIGL.addItem("°K")

        self.calculateButtonIGL.clicked.connect(self.calculateIdealGasLaw)

    def calculateIdealGasLaw(self):
        pressureUnit = self.pressureDropDownIGL.currentText()
        temperatureUnit = self.temperatureDropDownIGL.currentText()
        volumeUnit = self.volumeDropDownIGL.currentText()

        def _calculatePressure():
            try:
                pressure = (float(self.molesInputIGL.text()) * self.idealGasConstant * (float(
                    self.temperatureInputIGL.text()) + self.temperatureConversions[temperatureUnit])) / (float(
                    self.volumeInputIGL.text()) * self.volumeConversions[volumeUnit])
                return pressure
            except ValueError:
                return "Value Error"

        def _calculateVolume():
            try:
                volume = (float(self.molesInputIGL.text()) * self.idealGasConstant * (float(
                    self.temperatureInputIGL.text()) + self.temperatureConversions[temperatureUnit])) / (
                                 float(self.pressureInputIGL.text()) * self.pressureConversions[pressureUnit])
                return volume
            except ValueError:
                return "Value Error"

        def _calculateTemperature():
            try:
                temperature = ((float(self.pressureInputIGL.text()) * self.pressureConversions[pressureUnit]) * (float(
                    self.volumeInputIGL.text()) * self.volumeConversions[volumeUnit])) / (
                                      float(self.molesInputIGL.text()) * self.idealGasConstant)
                return temperature
            except ValueError:
                return "Value Error"

        def _calculateMoles():
            try:
                moles = ((float(self.pressureInputIGL.text()) * self.pressureConversions[pressureUnit]) * (
                        float(self.volumeInputIGL.text()) * self.volumeConversions[volumeUnit])) / (
                                self.idealGasConstant * (float(self.temperatureInputIGL.text()) +
                                                         self.temperatureConversions[temperatureUnit]))
                return moles
            except ValueError:
                return "Value Error"

        if self.pressureInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Pressure: {_calculatePressure()}")
        elif self.volumeInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Volume: {_calculateVolume()}")
        elif self.temperatureInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Temperature: {_calculateTemperature()}")
        elif self.molesInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Number of moles: {_calculateMoles()}")
        else:
            self.resultLabelIGL.setText("wtf are you doing mate")


class ChemBalancer(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.balancerLayout = QHBoxLayout()

        self.equationInput = QLineEdit()
        self.balanceButton = QPushButton()

        self.left = list()
        self.right = list()
        self.totalLeft = dict()
        self.totalRight = dict()

        self.integers = "0123456789"
        self.equationSplit = list()
        self.reactants = str()
        self.products = str()

        self.reactantComponents = list()
        self.productComponents = list()

        self.balancerLayout.addWidget(self.equationInput)
        self.balancerLayout.addWidget(self.balanceButton)

        self.balanceButton.clicked.connect(self.runBalancer)

    def runBalancer(self):
        print("#DEBUG# SPLIT")
        self.splitEquation()
        print("#DEBUG# GET REACTANTS")
        self.getReactants()
        print("#DEBUG# GET PRODUCTS")
        self.getProducts()

    def splitEquation(self):
        self.equationSplit = self.equationInput.text().split(" = ")

        print("#DEBUG# ", self.equationSplit)

        self.reactants = self.equationSplit[0]

        print("#DEBUG# ", self.reactants)

        try:
            self.products = self.equationSplit[1]
        except IndexError:
            print("User isn't the brightest")

        print("#DEBUG# ", self.products)

        self.reactantComponents = self.reactants.split(" + ")
        self.productComponents = self.products.split(" + ")

        print("#DEBUG# ", self.reactantComponents)
        print("#DEBUG# ", self.productComponents)

    def parseComponent(self, component, countsDict, totalDict):
        for i in range(len(component)):
            print("#DEBUG# ", component)
            print("#DEBUG# i = ", component[i])
            if component[0] in self.integers:
                print("#DEBUG# GOT INTEGER")
                try:
                    if component[0 + 1] in self.integers:
                        try:
                            if component[0 + 2] in self.integers:
                                coefficient = int(component[0: 0 + 3])
                            else:
                                coefficient = int(component[0: 0 + 2])
                        except IndexError:
                            coefficient = int(component[0: 0 + 2])
                    else:
                        coefficient = int(component[0])
                except IndexError:
                    coefficient = int(component[0])
            else:
                print("#DEBUG# NO INT")
                coefficient = 1
            if component[i].isupper():
                if component[i + 1].islower():
                    try:
                        if component[i + 2].islower():
                            element = component[i:(i + 3)]
                            print("#DEBUG# 1", element)
                        else:
                            element = component[i:(i + 2)]
                            print("#DEBUG# 2", element)
                            try:
                                if component[i + 2] in self.integers:
                                    try:
                                        if component[i + 3] in self.integers:
                                            try:
                                                if component[i + 4] in self.integers:
                                                    number = int(component[i + 2: i + 5])
                                            except IndexError:
                                                number = int(component[i + 2: i + 4])
                                    except IndexError:
                                        number = int(component[i + 2])
                                else:
                                    number = 1
                            except IndexError:
                                number = 1
                    except IndexError:
                        element = component[i:(i + 2)]
                        print("#DEBUG# INDEX ERROR ", element)
                else:
                    element = component[i]
                    print("#DEBUG# 3", element)
                    try:
                        print("#DEBUG# IN TRY")
                        if component[i + 1] in self.integers:
                            print("#DEBUG# IN TRY IF")
                            try:
                                if component[i + 2] in self.integers:
                                    print("#DEBUG# IN TRY IF2")
                                    try:
                                        if component[i + 3] in self.integers:
                                            number = int(component[i + 1: i + 4])
                                    except IndexError:
                                        number = int(component[i + 1: i + 3])
                                else:
                                    number = int(component[i + 1])
                            except IndexError:
                                number = int(component[i + 1])
                        else:
                            number = 1
                    except IndexError:
                        continue
                try:
                    if element in countsDict:
                        countsDict[element] += number * coefficient
                    else:
                        countsDict[element] = number * coefficient
                    if element in totalDict:
                        totalDict[element] += number * coefficient
                    else:
                        totalDict[element] = number * coefficient
                except UnboundLocalError:
                    continue

            else:
                print("#DEBUG# ###################", )
            print("#DEBUG# counts ", countsDict)
            print("#DEBUG# total ", totalDict)

    def getReactants(self):
        for component in self.reactantComponents:
            leftCounts = dict()
            self.parseComponent(component, leftCounts, self.totalLeft)
            self.left.append(leftCounts)

    def getProducts(self):
        for component in self.productComponents:
            rightCounts = dict()
            self.parseComponent(component, rightCounts, self.totalRight)
            self.right.append(rightCounts)


class TabBar(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QHBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.addTab(self.tab1, "Ideal Gas Law")
        self.tabs.addTab(self.tab2, "Tab2")
        self.tabs.addTab(self.tab3, "Tab3")
        self.tabs.addTab(self.tab4, "Tab4")
        self.tabs.addTab(self.tab5, "Tab5")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class InteractiveTable(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.tableLayout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.tableLayout.addWidget(self.table)

        self.addRowButton = QPushButton("Add Row")
        self.deleteRowButton = QPushButton("Delete Row")
        self.addColButton = QPushButton("Add Column")
        self.deleteColButton = QPushButton("Delete Column")

        self.tableLayout.addWidget(self.addRowButton)
        self.tableLayout.addWidget(self.deleteRowButton)
        self.tableLayout.addWidget(self.addColButton)
        self.tableLayout.addWidget(self.deleteColButton)

        self.addRowButton.clicked.connect(self.addRow)
        self.deleteRowButton.clicked.connect(self.delRow)
        self.addColButton.clicked.connect(self.addCol)
        self.deleteColButton.clicked.connect(self.delCol)

        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.createTable()

    def createTable(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.table.setItem(row, col, item)

    def addRow(self):
        currentRows = self.table.rowCount()
        self.table.setRowCount(currentRows + 1)

    def addCol(self):
        currentCols = self.table.columnCount()
        self.table.setColumnCount(currentCols + 1)

    def delRow(self):
        selectedRow = self.table.currentRow()
        if selectedRow >= 0:
            self.table.removeRow(selectedRow)

    def delCol(self):
        selectedCol = self.table.currentColumn()
        if selectedCol >= 0:
            self.table.removeColumn(selectedCol)


def main():
    app = QApplication(sys.argv)

    # Load CSS file
    app.setStyleSheet(open('style.css').read())
    mainWin = ChemBox()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
