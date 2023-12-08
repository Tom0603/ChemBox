from PyQt6.QtWidgets import QTabWidget, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


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
        self.tabs.addTab(self.tab5, "ChemEditor")

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


class SideBar(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.side_bar_layout = QVBoxLayout()

        # Create buttons
        self.moles_tab_button = QPushButton("Moles")
        self.conc_tab_button = QPushButton("Concentration")
        self.avogadro_tab_button = QPushButton("Avogadro's Calculator")
        self.ideal_gas_tab_button = QPushButton("Ideal Gas Equation")
        self.atom_econ_tab_button = QPushButton("Atom Economy")
        self.perc_yield_tab_button = QPushButton("% Yield")

        self.moles_tab_button.clicked.connect(self.moles_button)
        self.conc_tab_button.clicked.connect(self.conc_button)
        self.avogadro_tab_button.clicked.connect(self.avogadro_button)
        self.ideal_gas_tab_button.clicked.connect(self.ideal_gas_button)
        self.atom_econ_tab_button.clicked.connect(self.atom_econ_button)
        self.perc_yield_tab_button.clicked.connect(self.perc_yield_button)

        # Create tabs
        self.moles_tab = QWidget()
        self.conc_tab = QWidget()
        self.avogadro_tab = QWidget()
        self.ideal_gas_tab = QWidget()
        self.atom_econ_tab = QWidget()
        self.perc_yield_tab = QWidget()

        # Add buttons to sidebar layout
        self.side_bar_layout.addWidget(self.moles_tab_button)
        self.side_bar_layout.addWidget(self.conc_tab_button)
        self.side_bar_layout.addWidget(self.avogadro_tab_button)
        self.side_bar_layout.addWidget(self.ideal_gas_tab_button)
        self.side_bar_layout.addWidget(self.atom_econ_tab_button)
        self.side_bar_layout.addWidget(self.perc_yield_tab_button)

        self.side_bar_widget = QWidget()
        self.side_bar_widget.setLayout(self.side_bar_layout)

        self.page_widget = QTabWidget()

        self.page_widget.addTab(self.moles_tab, "")
        self.page_widget.addTab(self.conc_tab, "")
        self.page_widget.addTab(self.avogadro_tab, "")
        self.page_widget.addTab(self.ideal_gas_tab, "")
        self.page_widget.addTab(self.atom_econ_tab, "")
        self.page_widget.addTab(self.perc_yield_tab, "")

        self.page_widget.setCurrentIndex(0)
        self.page_widget.setStyleSheet('''QTabBar::tab{
        width: 0; 
        height: 0; 
        margin: 0; 
        padding: 0; 
        border: none;
        }''')

        self.main_layout = QHBoxLayout()
        self.main_layout.addWidget(self.side_bar_widget)
        self.main_layout.addWidget(self.page_widget)

        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

    # Define actions for each button

    def moles_button(self):
        self.page_widget.setCurrentIndex(0)

    def conc_button(self):
        self.page_widget.setCurrentIndex(1)

    def avogadro_button(self):
        self.page_widget.setCurrentIndex(2)

    def ideal_gas_button(self):
        self.page_widget.setCurrentIndex(3)

    def atom_econ_button(self):
        self.page_widget.setCurrentIndex(4)

    def perc_yield_button(self):
        self.page_widget.setCurrentIndex(5)
