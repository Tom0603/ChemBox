import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QGridLayout, QWidget, QPushButton, \
    QLineEdit, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem

import re
from sympy import Matrix, lcm


class ChemBox(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.left = 300
        self.top = 300
        self.width = 800
        self.height = 480
        self.title = "ChemBox"
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.tabBar = TabBar()
        self.setCentralWidget(self.tabBar)

        self.sideBar = SideBar()

        self.tabBar.tab1.setLayout(self.sideBar.mainLayout)

        # Initialise moles tab in sidebar
        self.amountOfSubstance = AmountOfSubstance()
        self.sideBar.molesTab.setLayout(self.amountOfSubstance.aosLayout)

        # Initialise igl tab in sidebar
        self.idealGasLaw = IdealGasLaw()
        self.sideBar.idealGasTab.setLayout(self.idealGasLaw.idealGasLayout)

        self.chemBalancer = ChemBalancer()
        self.tabBar.tab3.setLayout(self.chemBalancer.balancerLayout)

        # self.interactiveTable = InteractiveTable()
        # self.tabBar.tab2.setLayout(self.interactiveTable.tableLayout)


class AmountOfSubstance(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.aosLayout = QGridLayout()

        # Unit conversions
        self.massConversions = {
            "mg": 0.001,
            "g": 1,
            "kg": 1000,
            "t": 1000000
        }

        self.moleConversions = {
            "μmol": 0.000001,
            "mmol": 0.001,
            "mol": 1,
        }

        # Initialise moles calculation Layout
        self.molesLabel = QLabel("Moles:")
        self.massLabel = QLabel("Mass:")
        self.mrLabel = QLabel("Molecular weight:")

        self.molesInput = QLineEdit()
        self.massInput = QLineEdit()
        self.mrInput = QLineEdit()

        self.calculateButton = QPushButton("Calculate")
        self.calculateButton.clicked.connect(self.molesCalculation)

        self.massUnitDropdown = QComboBox()
        self.massUnitDropdown.addItem("mg")
        self.massUnitDropdown.addItem("g")
        self.massUnitDropdown.addItem("kg")
        self.massUnitDropdown.addItem("t")

        self.molesUnitDropdown = QComboBox()
        self.molesUnitDropdown.addItem("μmol")
        self.molesUnitDropdown.addItem("mmol")
        self.molesUnitDropdown.addItem("mol")

        self.aosLayout.addWidget(self.molesLabel, 0, 0)
        self.aosLayout.addWidget(self.massLabel, 1, 0)
        self.aosLayout.addWidget(self.mrLabel, 2, 0)

        self.aosLayout.addWidget(self.molesInput, 0, 1)
        self.aosLayout.addWidget(self.massInput, 1, 1)
        self.aosLayout.addWidget(self.mrInput, 2, 1)

        self.aosLayout.addWidget(self.molesUnitDropdown, 0, 2)
        self.aosLayout.addWidget(self.massUnitDropdown, 1, 2)

        self.aosLayout.addWidget(self.calculateButton, 3, 1)

    def getMolesLayout(self):
        pass

    def molesCalculation(self):
        massUnit = self.massUnitDropdown.currentText()
        molesUnit = self.molesUnitDropdown.currentText()

        if self.molesInput.text() == "":
            try:
                moles = (float(self.massInput.text()) * self.massConversions[massUnit]) / float(self.mrInput.text())
                self.molesInput.setText(str(moles))
                self.molesUnitDropdown.setCurrentText("mol")
            except ValueError:
                print("Value Error")
        if self.massInput.text() == "":
            try:
                mass = (float(self.molesInput.text()) * self.moleConversions[molesUnit]) * float(self.mrInput.text())
                self.massInput.setText(str(mass))
            except ValueError:
                print("Value Error")
        if self.mrInput.text() == "":
            try:
                mr = (float(self.massInput.text()) * self.massConversions[massUnit]) / (
                        float(self.molesInput.text()) * self.moleConversions[molesUnit])
                self.mrInput.setText(str(mr))
            except ValueError:
                print("Value Error")


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
    f"""
    This module of the {ChemBox} is responsible for balancing chemical equations.
    It parses user-provided chemical equations, identifies reactants and products, 
    and calculates the coefficients to achieve a balanced equation.
    The class utilizes SymPy for symbolic mathematics to find the null space and perform matrix operations, 
    ensuring accurate and balanced chemical equations.
    """

    def __init__(self):
        super(QWidget, self).__init__()
        self.balancerLayout = QVBoxLayout()

        self.equationInput = QLineEdit()
        self.balanceButton = QPushButton("Balance")
        self.balancedLabel = QLabel()

        # Add the widgets to the balancerLayout
        self.balancerLayout.addWidget(self.equationInput)
        self.balancerLayout.addWidget(self.balanceButton)
        self.balancerLayout.addWidget(self.balancedLabel)

        self.balanceButton.clicked.connect(self.runBalancer)

        self.strippedEquation = str()
        self.equationSplit = list()

        self.reactants = list()
        self.products = list()

        self.elementList = list()
        self.elementMatrix = list()

        self.balancedEquation = str()

    def clearVariables(self):
        """
        Clears all the used variables to avoid using data or values from previous calculations.
        """

        if len(self.equationSplit) != 0:
            self.equationSplit.clear()
        if len(self.reactants) != 0:
            self.reactants.clear()
        if len(self.products) != 0:
            self.products.clear()
        if len(self.elementList) != 0:
            self.elementList.clear()
        if len(self.elementMatrix) != 0:
            self.elementMatrix = []

        self.reactants = ""
        self.products = ""
        self.balancedEquation = ""

    def splitEquation(self):
        """
        Takes {self.equationInput}, strips it from all the whitespaces
        and splits it up into separate reactants and products.
        """

        # Strip equation from any whitespaces
        try:
            self.strippedEquation = "".join(self.equationInput.text().split())
        except IndexError:
            return None
        print(self.strippedEquation)

        # Split equation into reactants (self.equationSplit[0]) and products (self.equationSplit[1])
        self.equationSplit = self.strippedEquation.split("=")
        print(self.equationSplit)

        try:
            self.reactants = self.equationSplit[0].split("+")
        except IndexError:
            return None
        print(self.reactants)
        try:
            self.products = self.equationSplit[1].split("+")
        except IndexError:
            return None
        print(self.products)

    def findReagents(self, compound, index, side):
        """
        This Function finds separate reagents by removing brackets from the compounds
        and then calls self.findElements().

        :param compound: String of elements as compound (e.g. Ag3(Fe3O)4).
        :param index: Index position of row in matrix.
        :param side: "1" for reactants, "-1" for products.
        """

        # Split the compound by parentheses
        reagents = re.split("(\([A-Za-z0-9]*\)[0-9]*)", compound)
        for reagent in reagents:
            if reagent.startswith("("):
                # Extract the element within parentheses
                inner_compound = reagent[1:-1]
                # Get the subscript outside the brackets
                bracketSubscript = reagent.split(")", 1)[-1]
                if bracketSubscript:
                    bracketSubscript = int(bracketSubscript)
                else:
                    bracketSubscript = 1
                # Recursively find elements within the inner compound
                self.findElements(inner_compound, index, bracketSubscript, side)
            else:
                # No brackets, directly find elements
                bracketSubscript = 1
                self.findElements(reagent, index, bracketSubscript, side)

    def findElements(self, reagent, index, bracketSubscript, side):
        """
        Separates out elements and subscripts using a regex,
        then loops through the elements and calls the function addToMatrix().

        :param reagent: String of reagent (e.g. H2O).
        :param index: Index position of row in matrix.
        :param bracketSubscript: The subscript value outside the brackets. Equal to 1 if there are no brackets.
        :param side: "1" for reactants, "-1" for products.
        """

        # Use regex to separate elements and subscripts
        elementCounts = re.findall("([A-Z][a-z]*)([0-9]*)", reagent)
        for element, subscript in elementCounts:
            if not subscript:
                subscript = 1
            else:
                subscript = int(subscript)
            # Call addToMatrix for each element
            self.addToMatrix(element, index, bracketSubscript * subscript, side)

    def addToMatrix(self, element, index, count, side):
        """
        It adds the provided element with a specified count to the matrix at the given index.
        The 'side' parameter determines whether the element is part of the reactants (positive side)
        or products (negative side) in the chemical equation.

        :param element: The element symbol as in the periodic table (e.g. Na).
        :param index: Index position of row in matrix.
        :param count: Number of specific element to add to the matrix.
        :param side: "1" for reactants, "-1" for products.
        """
        print(element, index, count, side)
        if index == len(self.elementMatrix):
            print(self.elementMatrix)
            self.elementMatrix.append([])
            print(self.elementMatrix)
            for x in self.elementList:
                print(self.elementList)
                self.elementMatrix[index].append(0)
                print(self.elementMatrix)

        if element not in self.elementList:
            self.elementList.append(element)
            for i in range(len(self.elementMatrix)):
                self.elementMatrix[i].append(0)
                print(self.elementMatrix)

        column = self.elementList.index(element)
        self.elementMatrix[index][column] += count * side
        print(self.elementList)
        print(self.elementMatrix)

    def runBalancer(self):
        """
        This the core function of the ChemBalancer class,
        responsible for balancing chemical equations.
        It parses the user-provided equation, deciphers compounds,
        constructs a matrix, finds the null space for balancing coefficients,
        and computes the balanced equation.
        This function leverages SymPy for mathematical operations, ensuring accurate chemical equation balancing.
        """

        # Clear variables, in case the program was run before
        self.clearVariables()

        self.splitEquation()

        for i in range(len(self.reactants)):
            self.findReagents(self.reactants[i], i, 1)
        for i in range(len(self.products)):
            self.findReagents(self.products[i], i + len(self.reactants), -1)

        self.elementMatrix = Matrix(self.elementMatrix)
        self.elementMatrix = self.elementMatrix.transpose()
        try:
            num = self.elementMatrix.nullspace()[0]
        except IndexError:
            return None
        print(num)
        multiple = lcm([val.q for val in num])
        num = multiple * num
        print(num)

        coefficient = num.tolist()

        for i in range(len(self.reactants)):
            if coefficient[i][0] != 1:
                self.balancedEquation += str(coefficient[i][0]) + self.reactants[i]
            else:
                self.balancedEquation += self.reactants[i]
            if i < len(self.reactants) - 1:
                self.balancedEquation += " + "
        self.balancedEquation += " = "

        for i in range(len(self.products)):
            if coefficient[i + len(self.reactants)][0] != 1:
                self.balancedEquation += str(coefficient[i + len(self.reactants)][0]) + self.products[i]
            else:
                self.balancedEquation += self.products[i]
            if i < len(self.products) - 1:
                self.balancedEquation += " + "
        self.equationInput.setText(f"{self.balancedEquation}")


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
        self.tabs.addTab(self.tab1, "Amount of Substance")
        self.tabs.addTab(self.tab2, "Tab2")
        self.tabs.addTab(self.tab3, "Balancer")
        self.tabs.addTab(self.tab4, "Tab4")
        self.tabs.addTab(self.tab5, "Tab5")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class SideBar(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.sideBarLayout = QVBoxLayout()

        # Create buttons
        self.molesTabButton = QPushButton("Moles")
        self.concTabButton = QPushButton("Concentration")
        self.gasVolTabButton = QPushButton("Molar gas volume")
        self.numParticlesTabButton = QPushButton("Number of particles")
        self.idealGasTabButton = QPushButton("Ideal gas equation")
        self.atomEconTabButton = QPushButton("Atom economy")
        self.percYieldTabButton = QPushButton("% Yield")

        self.molesTabButton.clicked.connect(self.molesButton)
        self.concTabButton.clicked.connect(self.concButton)
        self.gasVolTabButton.clicked.connect(self.gasVolButton)
        self.numParticlesTabButton.clicked.connect(self.numParticlesButton)
        self.idealGasTabButton.clicked.connect(self.idealGasButton)
        self.atomEconTabButton.clicked.connect(self.atomEconButton)
        self.percYieldTabButton.clicked.connect(self.percYieldButton)

        # Create tabs
        self.molesTab = QWidget()
        self.concTab = QWidget()
        self.gasVolTab = QWidget()
        self.numParticlesTab = QWidget()
        self.idealGasTab = QWidget()
        self.atomEconTab = QWidget()
        self.percYieldTab = QWidget()

        # Add buttons to sidebar layout
        self.sideBarLayout.addWidget(self.molesTabButton)
        self.sideBarLayout.addWidget(self.concTabButton)
        self.sideBarLayout.addWidget(self.gasVolTabButton)
        self.sideBarLayout.addWidget(self.numParticlesTabButton)
        self.sideBarLayout.addWidget(self.idealGasTabButton)
        self.sideBarLayout.addWidget(self.atomEconTabButton)
        self.sideBarLayout.addWidget(self.percYieldTabButton)

        self.sideBarWidget = QWidget()
        self.sideBarWidget.setLayout(self.sideBarLayout)

        self.pageWidget = QTabWidget()

        self.pageWidget.addTab(self.molesTab, "")
        self.pageWidget.addTab(self.concTab, "")
        self.pageWidget.addTab(self.gasVolTab, "")
        self.pageWidget.addTab(self.numParticlesTab, "")
        self.pageWidget.addTab(self.idealGasTab, "")
        self.pageWidget.addTab(self.atomEconTab, "")
        self.pageWidget.addTab(self.percYieldTab, "")

        self.pageWidget.setCurrentIndex(0)
        self.pageWidget.setStyleSheet('''QTabBar::tab{
        width: 0; 
        height: 0; 
        margin: 0; 
        padding: 0; 
        border: none;
        }''')

        self.mainLayout = QHBoxLayout()
        self.mainLayout.addWidget(self.sideBarWidget)
        self.mainLayout.addWidget(self.pageWidget)

        self.mainWidget = QWidget()
        self.mainWidget.setLayout(self.mainLayout)

    # Define actions for each button

    def molesButton(self):
        self.pageWidget.setCurrentIndex(0)

    def concButton(self):
        self.pageWidget.setCurrentIndex(1)

    def gasVolButton(self):
        self.pageWidget.setCurrentIndex(2)

    def numParticlesButton(self):
        self.pageWidget.setCurrentIndex(3)

    def idealGasButton(self):
        self.pageWidget.setCurrentIndex(4)

    def atomEconButton(self):
        self.pageWidget.setCurrentIndex(5)

    def percYieldButton(self):
        self.pageWidget.setCurrentIndex(6)


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
