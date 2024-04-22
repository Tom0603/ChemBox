from PyQt6.QtWidgets import QTabWidget, QWidget, QHBoxLayout, QGridLayout, QFrame, QLabel, QLineEdit, QComboBox


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


class RateBox(QWidget):
    """
    This class contains the gui components for molecules for the RateCalculator.

    #########################################
    # Order of reaction: _______________    #
    # Concentration: ___________________    #
    #########################################
    """

    def __init__(self, symbol):
        super(QWidget, self).__init__()

        self.layout = QGridLayout()

        self.box = QFrame(self)
        self.box.setFrameStyle(0x0001)
        self.box.setLineWidth(3)

        self.box_layout = QGridLayout()

        self.order_label = QLabel("Order of reaction: ")
        self.conc_label = QLabel(f"Concentration {symbol}: ")

        self.order_input = QComboBox()

        self.order_input.addItem("First")
        self.order_input.addItem("Second")
        self.order_input.setCurrentIndex(0)

        self.conc_input = QLineEdit()

        self.layout.addWidget(self.order_label, 0, 0)
        self.layout.addWidget(self.order_input, 0, 1)
        self.layout.addWidget(self.conc_label, 1, 0)
        self.layout.addWidget(self.conc_input, 1, 1)

        self.box.setLayout(self.layout)
        self.box_layout.addWidget(self.box, 0, 0)


class RateResultBox(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QGridLayout()

        self.box = QFrame(self)
        self.box.setFrameStyle(0x0001)
        self.box.setLineWidth(3)

        self.box_layout = QGridLayout()

        self.total_order_label = QLabel("Total order of reaction: ")
        self.rate_constant_label = QLabel("Rate constant (k): ")
        self.rate_label = QLabel("Rate of reaction: ")

        self.total_order_input = QLineEdit()
        self.rate_constant_input = QLineEdit()
        self.rate_input = QLineEdit()

        self.layout.addWidget(self.total_order_label, 0, 0)
        self.layout.addWidget(self.total_order_input, 0, 1)
        self.layout.addWidget(self.rate_constant_label, 1, 0)
        self.layout.addWidget(self.rate_constant_input, 1, 1)
        self.layout.addWidget(self.rate_label, 2, 0)
        self.layout.addWidget(self.rate_input, 2, 1)

        self.box.setLayout(self.layout)
        self.box_layout.addWidget(self.box, 0, 0)
