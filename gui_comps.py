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


class ChemCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.side_bar_layout = QVBoxLayout()

        # Create buttons
        self.moles_tab_button = QPushButton("Moles")
        self.conc_tab_button = QPushButton("Concentration")
        self.avogadro_tab_button = QPushButton("Avogadro's Calculator")
        self.ideal_gas_tab_button = QPushButton("Ideal Gas Equation")
        self.equilibrium_tab_button = QPushButton("Equilibrium Constant")
        self.gibbs_free_energy_tab_button = QPushButton("Gibbs Free Energy Calculator")
        self.specific_heat_tab_button = QPushButton("Specific Heat Calculator")

        self.moles_tab_button.clicked.connect(self.moles_button)
        self.conc_tab_button.clicked.connect(self.conc_button)
        self.avogadro_tab_button.clicked.connect(self.avogadro_button)
        self.ideal_gas_tab_button.clicked.connect(self.ideal_gas_button)
        self.equilibrium_tab_button.clicked.connect(self.equilibrium_button)
        self.gibbs_free_energy_tab_button.clicked.connect(self.gibbs_free_energy_button)
        self.specific_heat_tab_button.clicked.connect(self.specific_heat_button)

        # Create tabs
        self.moles_tab = QWidget()
        self.conc_tab = QWidget()
        self.avogadro_tab = QWidget()
        self.ideal_gas_tab = QWidget()
        self.equilibrium_tab = QWidget()
        self.gibbs_free_energy_tab = QWidget()
        self.specific_heat_tab = QWidget()

        # Add buttons to sidebar layout
        self.side_bar_layout.addWidget(self.moles_tab_button)
        self.side_bar_layout.addWidget(self.conc_tab_button)
        self.side_bar_layout.addWidget(self.avogadro_tab_button)
        self.side_bar_layout.addWidget(self.ideal_gas_tab_button)
        self.side_bar_layout.addWidget(self.equilibrium_tab_button)
        self.side_bar_layout.addWidget(self.gibbs_free_energy_tab_button)
        self.side_bar_layout.addWidget(self.specific_heat_tab_button)

        self.side_bar_widget = QWidget()
        self.side_bar_widget.setLayout(self.side_bar_layout)

        self.page_widget = QTabWidget()

        self.page_widget.addTab(self.moles_tab, "")
        self.page_widget.addTab(self.conc_tab, "")
        self.page_widget.addTab(self.avogadro_tab, "")
        self.page_widget.addTab(self.ideal_gas_tab, "")
        self.page_widget.addTab(self.equilibrium_tab, "")
        self.page_widget.addTab(self.gibbs_free_energy_tab, "")
        self.page_widget.addTab(self.specific_heat_tab, "")

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

    def equilibrium_button(self):
        self.page_widget.setCurrentIndex(4)

    def gibbs_free_energy_button(self):
        self.page_widget.setCurrentIndex(5)

    def specific_heat_button(self):
        self.page_widget.setCurrentIndex(6)
