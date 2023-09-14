import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QVBoxLayout, QWidget, QPushButton, \
    QLineEdit, QLabel


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


class TabBar(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QVBoxLayout(self)

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
