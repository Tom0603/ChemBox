import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QGridLayout, QWidget, QPushButton, \
    QLineEdit, QLabel, QComboBox, QHBoxLayout, QVBoxLayout


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

        self.idealGasLayout = QGridLayout()
        self.showIdealGasLaw()

    def showIdealGasLaw(self):
        self.tabBar.tab1.setLayout(self.idealGasLayout)

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

        # self.pressureDropDownIGL.activated.connect(self.pressureUnit)
        # self.volumeDropDownIGL.activated.connect(self.pressureUnit)

        self.calculateButtonIGL.clicked.connect(self.calculateIdealGasLaw)

    def calculateIdealGasLaw(self):
        pressureUnit = self.pressureDropDownIGL.currentText()
        temperatureUnit = self.temperatureDropDownIGL.currentText()
        volumeUnit = self.volumeDropDownIGL.currentText()

        def calculatePressure():
            try:
                pressure = (float(self.molesInputIGL.text()) * self.idealGasConstant * (float(
                    self.temperatureInputIGL.text()) + self.temperatureConversions[temperatureUnit])) / (float(
                    self.volumeInputIGL.text()) * self.volumeConversions[volumeUnit])
                return pressure
            except ValueError:
                return "Value Error"

        def calculateVolume():
            try:
                volume = (float(self.molesInputIGL.text()) * self.idealGasConstant * (float(
                    self.temperatureInputIGL.text()) + self.temperatureConversions[temperatureUnit])) / (
                                 float(self.pressureInputIGL.text()) * self.pressureConversions[pressureUnit])
                return volume
            except ValueError:
                return "Value Error"

        def calculateTemperature():
            try:
                temperature = ((float(self.pressureInputIGL.text()) * self.pressureConversions[pressureUnit]) * (float(
                    self.volumeInputIGL.text()) * self.volumeConversions[volumeUnit])) / (
                                      float(self.molesInputIGL.text()) * self.idealGasConstant)
                return temperature
            except ValueError:
                return "Value Error"

        def calculateMoles():
            try:
                moles = ((float(self.pressureInputIGL.text()) * self.pressureConversions[pressureUnit]) * (
                        float(self.volumeInputIGL.text()) * self.volumeConversions[volumeUnit])) / (
                                self.idealGasConstant * (float(self.temperatureInputIGL.text()) +
                                self.temperatureConversions[temperatureUnit]))
                return moles
            except ValueError:
                return "Value Error"

        if self.pressureInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Pressure: {calculatePressure()}")
        elif self.volumeInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Volume: {calculateVolume()}")
        elif self.temperatureInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Temperature: {calculateTemperature()}")
        elif self.molesInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Number of moles: {calculateMoles()}")
        else:
            self.resultLabelIGL.setText("wtf are you doing mate")


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


def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(open('style.css').read())  # Load your CSS file
    mainWin = ChemBox()
    mainWin.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
