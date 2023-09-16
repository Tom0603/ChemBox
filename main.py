import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QGridLayout, QWidget, QPushButton, \
    QLineEdit, QLabel, QComboBox, QHBoxLayout


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

        self.pressureDropDownIGL = QComboBox()
        self.volumeDropDownIGL = QComboBox()
        self.temperatureDropDownIGL = QComboBox()

        self.idealGasLayout = QGridLayout()
        self.showIdealGasLaw()

    def activated(self, index):
        print(f"Activated index: {index}")

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

        self.calculateButtonIGL.clicked.connect(self.calculateIdealGasLaw)

        self.pressureDropDownIGL.addItem("One")
        self.pressureDropDownIGL.addItem("Two")
        self.pressureDropDownIGL.addItem("Three")
        self.pressureDropDownIGL.addItem("Four")

        self.volumeDropDownIGL.addItem("One")
        self.volumeDropDownIGL.addItem("Two")
        self.volumeDropDownIGL.addItem("Three")
        self.volumeDropDownIGL.addItem("Four")

        self.temperatureDropDownIGL.addItem("One")
        self.temperatureDropDownIGL.addItem("Two")
        self.temperatureDropDownIGL.addItem("Three")
        self.temperatureDropDownIGL.addItem("Four")

        self.pressureDropDownIGL.activated.connect(self.activated)
        self.volumeDropDownIGL.activated.connect(self.activated)

    def calculateIdealGasLaw(self):
        def calculatePressure():
            pressure = (float(self.molesInputIGL.text()) * self.idealGasConstant * float(
                self.temperatureInputIGL.text())) // float(self.volumeInputIGL.text())
            return pressure

        def calculateVolume():
            volume = (float(self.molesInputIGL.text()) * self.idealGasConstant * float(
                self.temperatureInputIGL.text())) / float(self.pressureInputIGL.text())
            return volume

        def calculateTemperature():
            temperature = (float(self.pressureInputIGL.text()) * float(self.volumeInputIGL.text())) / (
                    float(self.molesInputIGL.text()) * self.idealGasConstant)
            return temperature

        if self.pressureInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Pressure: {calculatePressure()}")
        elif self.volumeInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Volume: {calculateVolume()}")
        elif self.temperatureInputIGL.text() == "":
            self.resultLabelIGL.setText(f"Temperature: {calculateTemperature()}")
        else:
            self.resultLabelIGL.setText("wtf")


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
