import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from chem_editor_gui import ChemEditor

from chem_calculator import MolesCalculator, ConcCalculator, AvogadroCalculator, IdealGasLawCalculator, \
    EquilibriumCalculator, GibbsFreeEnergyCalculator, SpecificHeatCalculator

from chem_balancer import ChemBalancer
from gui_comps import TabBar, ChemCalculator


class ChemBox(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.__left = 300
        self.__top = 300
        self.__width = 1280
        self.__height = 720
        self.__title = "ChemBox"
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)

        self.tab_bar = TabBar()
        self.setCentralWidget(self.tab_bar)

        self.chem_calculator = ChemCalculator()

        self.tab_bar.tab1.setLayout(self.chem_calculator.main_layout)

        self.moles_calc = MolesCalculator()
        self.concentration_calc = ConcCalculator()
        self.avogadro_calc = AvogadroCalculator()
        self.ideal_gas_law_calc = IdealGasLawCalculator()
        self.equilibrium_calc = EquilibriumCalculator()
        self.gibbs_calc = GibbsFreeEnergyCalculator()
        self.specific_heat_calc = SpecificHeatCalculator()

        # Initialise moles tab in sidebar
        self.chem_calculator.moles_tab.setLayout(self.moles_calc.moles_layout)

        # Initialise concentration tab in sidebar
        self.chem_calculator.conc_tab.setLayout(self.concentration_calc.conc_layout)

        # Initialise avogadro's calculator tab in sidebar
        self.chem_calculator.avogadro_tab.setLayout(self.avogadro_calc.avogadro_layout)

        # Initialise igl tab in sidebar
        self.chem_calculator.ideal_gas_tab.setLayout(self.ideal_gas_law_calc.ideal_gas_layout)

        # Initialise equilibrium constant calculator tab
        self.chem_calculator.equilibrium_tab.setLayout(self.equilibrium_calc.layout)

        # Initialise gibbs free energy calculator
        self.chem_calculator.gibbs_free_energy_tab.setLayout(self.gibbs_calc.layout)

        # Initialise specific heat energy calculator
        self.chem_calculator.specific_heat_tab.setLayout(self.specific_heat_calc.layout)

        self.chem_balancer = ChemBalancer()
        self.tab_bar.tab2.setLayout(self.chem_balancer.balancer_layout)

        self.chem_editor = ChemEditor()
        self.tab_bar.tab3.setLayout(self.chem_editor.editor_layout)


def main():
    app = QApplication(sys.argv)

    # Load CSS file
    app.setStyleSheet(open('style.css').read())

    main_win = ChemBox()
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
