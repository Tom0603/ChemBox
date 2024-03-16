from PyQt6.QtWidgets import QTabWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class TabBar(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QHBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tabs.addTab(self.tab1, "ChemCalculator")
        self.tabs.addTab(self.tab2, "ChemBalancer")
        self.tabs.addTab(self.tab3, "ChemEditor")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
