from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QHBoxLayout, QTabWidget, \
    QVBoxLayout, QMessageBox

from math import log

import re

from gui_comps import RateBox, RateResultBox


def is_numeric(user_input):
    if not user_input:
        return True
    # Regular expression to match integers or decimals
    pattern = r'^[-+]?[0-9]*\.?[0-9]+$'
    print(user_input)
    print(bool(re.match(pattern, user_input)))
    return bool(re.match(pattern, user_input))


def find_empty_input(input_list: list[QLineEdit]) -> QLineEdit | None:
    """
    An algorithm for finding the empty input out of a list of inputs.
    Only works when looking for a single empty input.
    """

    count = 0
    empty = None

    for i in range(len(input_list)):
        if not input_list[i].text().strip():
            count += 1
            empty = input_list[i]

    if count == 1:
        return empty


def check_invalid_symbol(input_list: list[QLineEdit]) -> bool:
    """
    An algorithm for checking for invalid symbols.
    """

    invalid = False

    for i in range(len(input_list)):
        if not is_numeric(input_list[i].text().strip()):
            invalid = True

    return invalid


def show_dialog(message):
    dlg = QMessageBox()
    dlg.setWindowTitle("Invalid Input!")
    dlg.setText(f"Invalid user input!\n {message}")
    dlg.setIcon(QMessageBox.Icon.Critical)
    button = dlg.exec()

    if button == QMessageBox.StandardButton.Ok:
        print("OK!")


class ChemCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.side_bar_layout = QVBoxLayout()

        self.moles_calc = MolesCalculator()
        self.concentration_calc = ConcCalculator()
        self.avogadro_calc = AvogadroCalculator()
        self.ideal_gas_law_calc = IdealGasLawCalculator()
        self.equilibrium_calc = EquilibriumCalculator()
        self.gibbs_calc = GibbsFreeEnergyCalculator()
        self.specific_heat_calc = SpecificHeatCalculator()
        self.rate_calc = RateCalculator()

        # Create buttons
        self.moles_tab_button = QPushButton("Moles")
        self.conc_tab_button = QPushButton("Concentration")
        self.avogadro_tab_button = QPushButton("Avogadro's Calculator")
        self.ideal_gas_tab_button = QPushButton("Ideal Gas Equation")
        self.equilibrium_tab_button = QPushButton("Equilibrium Constant")
        self.gibbs_free_energy_tab_button = QPushButton("Gibbs Free Energy Calculator")
        self.specific_heat_tab_button = QPushButton("Specific Heat Calculator")
        self.rate_tab_button = QPushButton("Rate Constant")

        self.moles_tab_button.clicked.connect(self.moles_action)
        self.conc_tab_button.clicked.connect(self.conc_action)
        self.avogadro_tab_button.clicked.connect(self.avogadro_action)
        self.ideal_gas_tab_button.clicked.connect(self.ideal_gas_action)
        self.equilibrium_tab_button.clicked.connect(self.equilibrium_action)
        self.gibbs_free_energy_tab_button.clicked.connect(self.gibbs_free_energy_action)
        self.specific_heat_tab_button.clicked.connect(self.specific_heat_action)
        self.rate_tab_button.clicked.connect(self.rate_action)

        # Create tabs
        self.moles_tab = QWidget()
        self.conc_tab = QWidget()
        self.avogadro_tab = QWidget()
        self.ideal_gas_tab = QWidget()
        self.equilibrium_tab = QWidget()
        self.gibbs_free_energy_tab = QWidget()
        self.specific_heat_tab = QWidget()
        self.rate_tab = QWidget()

        # Initialise moles tab in sidebar
        self.moles_tab.setLayout(self.moles_calc.moles_layout)

        # Initialise concentration tab in sidebar
        self.conc_tab.setLayout(self.concentration_calc.layout)

        # Initialise avogadro's calculator tab in sidebar
        self.avogadro_tab.setLayout(self.avogadro_calc.layout)

        # Initialise igl tab in sidebar
        self.ideal_gas_tab.setLayout(self.ideal_gas_law_calc.ideal_gas_layout)

        # Initialise equilibrium constant calculator tab
        self.equilibrium_tab.setLayout(self.equilibrium_calc.layout)

        # Initialise gibbs free energy calculator
        self.gibbs_free_energy_tab.setLayout(self.gibbs_calc.layout)

        # Initialise specific heat energy calculator
        self.specific_heat_tab.setLayout(self.specific_heat_calc.layout)

        # Initialise rate constant calculator
        self.rate_tab.setLayout(self.rate_calc.layout)

        # Add buttons to sidebar layout
        self.side_bar_layout.addWidget(self.moles_tab_button)
        self.side_bar_layout.addWidget(self.conc_tab_button)
        self.side_bar_layout.addWidget(self.avogadro_tab_button)
        self.side_bar_layout.addWidget(self.ideal_gas_tab_button)
        self.side_bar_layout.addWidget(self.equilibrium_tab_button)
        self.side_bar_layout.addWidget(self.gibbs_free_energy_tab_button)
        self.side_bar_layout.addWidget(self.specific_heat_tab_button)
        self.side_bar_layout.addWidget(self.rate_tab_button)

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
        self.page_widget.addTab(self.rate_tab, "")

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

    def moles_action(self):
        self.page_widget.setCurrentIndex(0)

    def conc_action(self):
        self.page_widget.setCurrentIndex(1)

    def avogadro_action(self):
        self.page_widget.setCurrentIndex(2)

    def ideal_gas_action(self):
        self.page_widget.setCurrentIndex(3)

    def equilibrium_action(self):
        self.page_widget.setCurrentIndex(4)

    def gibbs_free_energy_action(self):
        self.page_widget.setCurrentIndex(5)

    def specific_heat_action(self):
        self.page_widget.setCurrentIndex(6)

    def rate_action(self):
        self.page_widget.setCurrentIndex(7)


class MolesCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.moles_layout = QGridLayout()

        # Unit conversions
        self.mass_conversions = {
            "mg": 0.001,
            "g": 1,
            "kg": 1000,
            "t": 1000000
        }

        self.mole_conversions = {
            "μmol": 0.000001,
            "mmol": 0.001,
            "mol": 1,
        }

        self.volume_conversions = {
            "cm³": 0.001,
            "dm³": 1.0,
            "m³": 1000.0,

        }

        # Initialise moles calculation Layout
        self.moles_label = QLabel("Moles:")
        self.mass_label = QLabel("Mass:")
        self.mr_label = QLabel("Molecular weight:")

        self.moles_input = QLineEdit()
        self.mass_input = QLineEdit()
        self.mr_input = QLineEdit()

        self.input_list = [self.moles_input, self.mass_input, self.mr_input]

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        self.mass_unit_dropdown = QComboBox()
        self.mass_unit_dropdown.addItem("mg")
        self.mass_unit_dropdown.addItem("g")
        self.mass_unit_dropdown.addItem("kg")
        self.mass_unit_dropdown.addItem("t")

        self.mass_unit_dropdown.setCurrentIndex(1)

        self.moles_unit_dropdown = QComboBox()
        self.moles_unit_dropdown.addItem("μmol")
        self.moles_unit_dropdown.addItem("mmol")
        self.moles_unit_dropdown.addItem("mol")

        self.moles_unit_dropdown.setCurrentIndex(2)

        self.get_moles_layout()

    def calculate(self):
        """
        This function routes to the correct calculation, which is then performed.
        """

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        mass_unit = self.mass_conversions[self.mass_unit_dropdown.currentText()]
        moles_unit = self.mole_conversions[self.moles_unit_dropdown.currentText()]

        to_calc = find_empty_input(self.input_list.copy())

        if to_calc is self.moles_input:
            self.calculate_moles(mass_unit)
        elif to_calc is self.mass_input:
            self.calculate_mass(moles_unit)
        elif to_calc is self.mr_input:
            self.calculate_mr(mass_unit, moles_unit)
        else:
            return

    def calculate_moles(self, mass_unit):
        """
        Calculates the moles and calls for an update of the gui input and adjusts the moles unit dropdown.
        """

        moles = (float(self.mass_input.text()) * mass_unit) / float(self.mr_input.text())
        self.update_input(moles)
        self.moles_unit_dropdown.setCurrentIndex(2)

    def calculate_mass(self, moles_unit):
        """
        Calculates the mass and calls for an update of the gui input and adjusts the moles unit dropdown.
        """

        mass = (float(self.moles_input.text()) * moles_unit) * float(
            self.mr_input.text())
        self.update_input(mass)
        self.mass_unit_dropdown.setCurrentIndex(1)

    def calculate_mr(self, mass_unit, moles_unit):
        """
        Calculates the mr and calls for an update of the gui input.
        """

        mr = (float(self.mass_input.text()) * mass_unit) / (
                float(self.moles_input.text()) * moles_unit)
        self.update_input(mr)

    def update_input(self, result):
        """
        Uses the find_empty_input() function to find the empty input, and then updates it using the result parameter.
        """

        find_empty_input(self.input_list.copy()).setText(str(result))

    def get_moles_layout(self):
        f"""
        This function adds all the essential widgets to the {self.moles_layout} 
        """

        self.moles_layout.addWidget(self.moles_label, 0, 0)
        self.moles_layout.addWidget(self.mass_label, 1, 0)
        self.moles_layout.addWidget(self.mr_label, 2, 0)

        self.moles_layout.addWidget(self.moles_input, 0, 1)
        self.moles_layout.addWidget(self.mass_input, 1, 1)
        self.moles_layout.addWidget(self.mr_input, 2, 1)

        self.moles_layout.addWidget(self.moles_unit_dropdown, 0, 2)
        self.moles_layout.addWidget(self.mass_unit_dropdown, 1, 2)

        self.moles_layout.addWidget(self.calculate_button, 3, 1)


class ConcCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QGridLayout()

        # Unit conversions
        self.mole_conversions = {
            "μmol": 0.000001,
            "mmol": 0.001,
            "mol": 1,
        }

        self.volume_conversions = {
            "cm³": 0.001,
            "dm³": 1.0,
            "m³": 1000.0,

        }

        # Initialise concentration calculation Layout
        self.conc_label = QLabel("Concentration:")
        self.moles_label = QLabel("Moles:")
        self.vol_label = QLabel("Volume:")

        self.conc_input = QLineEdit()
        self.moles_input = QLineEdit()
        self.vol_input = QLineEdit()

        self.input_list = [self.conc_input, self.moles_input, self.vol_input]

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        self.moles_unit_dropdown = QComboBox()
        self.moles_unit_dropdown.addItem("μmol")
        self.moles_unit_dropdown.addItem("mmol")
        self.moles_unit_dropdown.addItem("mol")

        self.moles_unit_dropdown.setCurrentIndex(2)

        self.vol_unit_drop_down = QComboBox()
        self.vol_unit_drop_down.addItem("cm³")
        self.vol_unit_drop_down.addItem("dm³")
        self.vol_unit_drop_down.addItem("m³")

        self.vol_unit_drop_down.setCurrentIndex(1)

        self.get_conc_layout()

    def calculate(self):
        """
        This function routes to the correct calculation, which is then performed.
        """

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        moles_unit = self.mole_conversions[self.moles_unit_dropdown.currentText()]
        vol_unit = self.volume_conversions[self.vol_unit_drop_down.currentText()]

        to_calc = find_empty_input(self.input_list.copy())

        if to_calc is self.moles_input:
            self.calculate_moles(vol_unit)
        elif to_calc is self.vol_input:
            self.calculate_vol(moles_unit)
        elif to_calc is self.conc_input:
            self.calculate_conc(moles_unit, vol_unit)
        else:
            return

    def calculate_moles(self, vol_unit):
        """
        Calculates the moles and calls for an update of the gui input and adjusts the moles unit dropdown.
        """

        moles = float(self.conc_input.text()) * (
                float(self.vol_input.text()) * vol_unit)
        self.update_input(moles)
        self.moles_unit_dropdown.setCurrentIndex(2)

    def calculate_vol(self, moles_unit):
        """
        Calculates the volume and calls for an update of the gui input.
        """

        vol = (float(self.moles_input.text()) * moles_unit) / float(
            self.conc_input.text())
        self.update_input(vol)
        self.vol_unit_drop_down.setCurrentIndex(1)

    def calculate_conc(self, moles_unit, vol_unit):
        """
        Calculates the concentration and calls for an update of the gui input.
        """

        conc = (float(self.moles_input.text()) * moles_unit) / (
                float(self.vol_input.text()) * vol_unit)
        self.update_input(conc)

    def update_input(self, result):
        """
        Uses the find_empty_input() function to find the empty input, and then updates it using the result parameter.
        """

        find_empty_input(self.input_list).setText(str(result))

    def get_conc_layout(self):
        """
           This function adds all the essential widgets to the layout.
           """

        self.layout.addWidget(self.conc_label, 0, 0)
        self.layout.addWidget(self.moles_label, 1, 0)
        self.layout.addWidget(self.vol_label, 2, 0)

        self.layout.addWidget(self.conc_input, 0, 1)
        self.layout.addWidget(self.moles_input, 1, 1)
        self.layout.addWidget(self.vol_input, 2, 1)

        self.layout.addWidget(self.moles_unit_dropdown, 1, 2)
        self.layout.addWidget(self.vol_unit_drop_down, 2, 2)

        self.layout.addWidget(self.calculate_button, 3, 1)


class AvogadroCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QGridLayout()

        self.avogadros_constant = 6.02214076

        # Unit conversions
        self.mass_conversions = {
            "mg": 0.001,
            "g": 1,
            "kg": 1000,
            "t": 1000000
        }

        self.mole_conversions = {
            "μmol": 0.000001,
            "mmol": 0.001,
            "mol": 1,
        }

        self.volume_conversions = {
            "cm³": 0.001,
            "dm³": 1.0,
            "m³": 1000.0,

        }

        # Initialise Avogadro's calculator
        self.mass_label = QLabel("Mass:")
        self.moles_label = QLabel("Moles:")
        self.molecular_weight_label = QLabel("Molecular weight:")
        self.num_atoms_label = QLabel("Number of atoms:")

        self.mass_input = QLineEdit()
        self.moles_input = QLineEdit()
        self.molecular_weight_input = QLineEdit()
        self.num_atoms_input = QLineEdit()

        self.input_list = [self.mass_input, self.moles_input, self.molecular_weight_input, self.num_atoms_input]

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        self.mass_unit_dropdown = QComboBox()
        self.mass_unit_dropdown.addItem("mg")
        self.mass_unit_dropdown.addItem("g")
        self.mass_unit_dropdown.addItem("kg")
        self.mass_unit_dropdown.addItem("t")

        self.mass_unit_dropdown.setCurrentIndex(1)

        # Initialise Atom Economy calculator

        self.get_layout()

    def get_layout(self):
        f"""
        This function adds all the essential widgets to the {self.layout} 
        """

        self.layout.addWidget(self.mass_label, 0, 0)
        self.layout.addWidget(self.moles_label, 1, 0)
        self.layout.addWidget(self.molecular_weight_label, 2, 0)
        self.layout.addWidget(self.num_atoms_label, 3, 0)

        self.layout.addWidget(self.mass_input, 0, 1)
        self.layout.addWidget(self.moles_input, 1, 1)
        self.layout.addWidget(self.molecular_weight_input, 2, 1)
        self.layout.addWidget(self.num_atoms_input, 3, 1)

        self.layout.addWidget(self.mass_unit_dropdown, 0, 2)

        self.layout.addWidget(self.calculate_button, 4, 1)

    def calculate(self):
        mass_unit = self.mass_unit_dropdown.currentText()

        if not find_empty_input(self.input_list.copy()):
            print("ououiuouo")
            if not self.mass_input.text():
                if self.moles_input.text() and self.molecular_weight_input.text():
                    self.update_mass(str(self.calculate_mass()))
            if not self.moles_input.text():
                if self.num_atoms_input.text():
                    self.update_moles(str(self.calculate_moles(mass_unit)))
                elif self.mass_input.text() and self.molecular_weight_input.text():
                    self.update_moles(str(self.calculate_moles(mass_unit)))
            if not self.molecular_weight_input.text():
                if self.mass_input.text() and self.moles_input.text():
                    self.update_mol_weight(str(self.calculate_mol_weight(mass_unit)))
            if self.num_atoms_input.text() == "":
                print("pleaaaaassee")
                if self.moles_input.text() != "":
                    print("allooooo")
                    self.update_num_atoms(str(self.calculate_num_atoms()))
                else:
                    show_dialog("Must leave one input line empty for it to be calculated!")
                    return
            else:
                show_dialog("Must leave one input line empty for it to be calculated!")
                return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        to_calc = find_empty_input(self.input_list.copy())

        if to_calc is self.mass_input:
            self.update_mass(str(self.calculate_mass()))
        if to_calc is self.moles_input:
            self.update_moles(str(self.calculate_moles(mass_unit)))
        if to_calc is self.molecular_weight_input:
            self.update_mol_weight(str(self.calculate_mol_weight(mass_unit)))
        if to_calc is self.num_atoms_input:
            self.update_num_atoms(str(self.calculate_num_atoms()))

    def calculate_mass(self):
        mass = float(self.moles_input.text()) * float(self.molecular_weight_input.text())
        return mass

    def calculate_moles(self, mass_unit):
        try:
            moles = float(self.num_atoms_input.text()) / self.avogadros_constant
        except ValueError:
            try:
                moles = (float(self.mass_input.text()) * self.mass_conversions[mass_unit]) / float(
                    self.molecular_weight_input.text())
                return moles
            except ValueError:
                return ""
        return moles

    def calculate_mol_weight(self, mass_unit):
        mol_weight = (float(self.mass_input.text()) * self.mass_conversions[mass_unit]) / float(
            self.moles_input.text())
        return mol_weight

    def calculate_num_atoms(self):
        num_atoms = float(self.moles_input.text()) * self.avogadros_constant
        return num_atoms

    def update_mass(self, mass):
        self.mass_input.setText(mass)

    def update_moles(self, moles):
        self.moles_input.setText(moles)

    def update_mol_weight(self, mol_weight):
        self.molecular_weight_input.setText(mol_weight)

    def update_num_atoms(self, num_atoms):
        self.num_atoms_input.setText(num_atoms)


class IdealGasLawCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.ideal_gas_layout = QGridLayout()

        # Initialise Ideal Gas Law (IGL) properties
        self.ideal_gas_constant = 8.314

        self.pressure_input = QLineEdit()
        self.volume_input = QLineEdit()
        self.temperature_input = QLineEdit()
        self.moles_input = QLineEdit()

        self.input_list = [self.pressure_input, self.volume_input, self.temperature_input, self.moles_input]

        self.pressure_label_igl = QLabel("Pressure:")
        self.volume_label_igl = QLabel("Volume:")
        self.temperature_label_igl = QLabel("Temperature:")
        self.moles_label_igl = QLabel("Amount of substance - moles:")
        self.calculate_button_igl = QPushButton('Calculate')

        self.pressure_conversions = {
            "Pa": 1.0,
            "kPa": 1000.0,
        }

        self.temperature_conversions = {
            "°C": 273.15,
            "°K": 0.0,
        }

        self.volume_conversions = {
            "cm³": 0.000001,
            "dm³": 0.001,
            "m³": 1.0,

        }

        self.pressure_drop_down_igl = QComboBox()
        self.volume_drop_down_igl = QComboBox()
        self.temperature_drop_down_igl = QComboBox()

        self.ideal_gas_layout.addWidget(self.pressure_label_igl, 0, 0)
        self.ideal_gas_layout.addWidget(self.pressure_input, 0, 1)
        self.ideal_gas_layout.addWidget(self.pressure_drop_down_igl, 0, 2)

        self.ideal_gas_layout.addWidget(self.volume_label_igl, 1, 0)
        self.ideal_gas_layout.addWidget(self.volume_input, 1, 1)
        self.ideal_gas_layout.addWidget(self.volume_drop_down_igl, 1, 2)

        self.ideal_gas_layout.addWidget(self.temperature_label_igl, 2, 0)
        self.ideal_gas_layout.addWidget(self.temperature_input, 2, 1)
        self.ideal_gas_layout.addWidget(self.temperature_drop_down_igl, 2, 2)

        self.ideal_gas_layout.addWidget(self.moles_label_igl, 3, 0)
        self.ideal_gas_layout.addWidget(self.moles_input, 3, 1)
        self.ideal_gas_layout.addWidget(self.calculate_button_igl, 4, 0)

        self.pressure_drop_down_igl.addItem("Pa")
        self.pressure_drop_down_igl.addItem("kPa")

        self.pressure_drop_down_igl.setCurrentIndex(0)

        self.volume_drop_down_igl.addItem("cm³")
        self.volume_drop_down_igl.addItem("dm³")
        self.volume_drop_down_igl.addItem("m³")

        self.volume_drop_down_igl.setCurrentIndex(2)

        self.temperature_drop_down_igl.addItem("°C")
        self.temperature_drop_down_igl.addItem("°K")

        self.temperature_drop_down_igl.setCurrentIndex(1)

        self.calculate_button_igl.clicked.connect(self.calculate_ideal_gas_law)

    def calculate_ideal_gas_law(self):
        pressure_unit = self.pressure_drop_down_igl.currentText()
        temperature_unit = self.temperature_drop_down_igl.currentText()
        volume_unit = self.volume_drop_down_igl.currentText()

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        to_calc = find_empty_input(self.input_list.copy())

        if to_calc is self.pressure_input:
            self.pressure_input.setText(str(self.calculate_pressure(temperature_unit, volume_unit)))
        elif to_calc is self.volume_input:
            self.volume_input.setText(str(self.calculate_volume(temperature_unit, pressure_unit)))
        elif to_calc is self.temperature_input:
            self.temperature_input.setText(str(self.calculate_temperature(pressure_unit, volume_unit)))
        elif to_calc is self.moles_input:
            self.moles_input.setText(str(self.calculate_moles(temperature_unit, volume_unit, pressure_unit)))

    def calculate_pressure(self, temperature_unit, volume_unit):
        pressure = (float(self.moles_input.text()) * self.ideal_gas_constant * (float(
            self.temperature_input.text()) + self.temperature_conversions[temperature_unit])) / (
                           float(self.volume_input.text()) * self.volume_conversions[volume_unit])
        return pressure

    def calculate_volume(self, temperature_unit, pressure_unit):
        volume = (float(self.moles_input.text()) * self.ideal_gas_constant * (float(
            self.temperature_input.text()) + self.temperature_conversions[temperature_unit])) / (
                         float(self.pressure_input.text()) * self.pressure_conversions[pressure_unit])
        return volume

    def calculate_temperature(self, pressure_unit, volume_unit):
        temperature = ((float(self.pressure_input.text()) * self.pressure_conversions[pressure_unit]) * (
                float(
                    self.volume_input.text()) * self.volume_conversions[volume_unit])) / (
                              float(self.moles_input.text()) * self.ideal_gas_constant)
        return temperature

    def calculate_moles(self, temperature_unit, volume_unit, pressure_unit):
        moles = ((float(self.pressure_input.text()) * self.pressure_conversions[pressure_unit]) * (
                float(self.volume_input.text()) * self.volume_conversions[volume_unit])) / (
                        self.ideal_gas_constant * (float(self.temperature_input.text()) +
                                                   self.temperature_conversions[temperature_unit]))
        return moles


class EquilibriumCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QGridLayout()

        # Set up line edits and labels
        self.equation_label = QLabel("a[A] + b[B] ⇌ c[C] + d[D]")
        self.equation_label.setFont(QFont("SansSerif", 22))
        self.equation_label.setStyleSheet("color: darkGray;")

        self.calc_button = QPushButton("Calculate")
        self.calc_button.clicked.connect(self.check_empty_input)

        self.conc_a_label = QLabel("Concentration [A]:")
        self.conc_a = QLineEdit()

        self.conc_b_label = QLabel("Concentration [B]:")
        self.conc_b = QLineEdit()

        self.conc_c_label = QLabel("Concentration [C]:")
        self.conc_c = QLineEdit()

        self.conc_d_label = QLabel("Concentration [D]:")
        self.conc_d = QLineEdit()

        self.coeff_a_label = QLabel("Coefficient a:")
        self.coeff_a = QLineEdit()

        self.coeff_b_label = QLabel("Coefficient b:")
        self.coeff_b = QLineEdit()

        self.coeff_c_label = QLabel("Coefficient c:")
        self.coeff_c = QLineEdit()

        self.coeff_d_label = QLabel("Coefficient d:")
        self.coeff_d = QLineEdit()

        self.equilibrium_constant_label = QLabel("Equilibrium Constant k:")
        self.equilibrium_constant = QLineEdit()

        self.input_list = [self.conc_a, self.conc_b, self.conc_c, self.conc_d, self.coeff_a, self.coeff_b, self.coeff_c,
                           self.coeff_d, self.equilibrium_constant]
        self.concentration_list = [self.conc_a, self.conc_b, self.conc_c, self.conc_d]
        self.coeff_list = [self.coeff_a, self.coeff_b, self.coeff_c, self.coeff_d]

        self.calculated_value = None

        self.layout.addWidget(self.equation_label, 0, 0)
        self.layout.addWidget(self.calc_button, 10, 0, 2, 0)

        self.layout.addWidget(self.conc_a_label, 1, 0)
        self.layout.addWidget(self.conc_a, 1, 1)
        self.layout.addWidget(self.coeff_a_label, 2, 0)
        self.layout.addWidget(self.coeff_a, 2, 1)
        self.layout.addWidget(self.conc_b_label, 3, 0)
        self.layout.addWidget(self.conc_b, 3, 1)
        self.layout.addWidget(self.coeff_b_label, 4, 0)
        self.layout.addWidget(self.coeff_b, 4, 1)
        self.layout.addWidget(self.conc_c_label, 5, 0)
        self.layout.addWidget(self.conc_c, 5, 1)
        self.layout.addWidget(self.coeff_c_label, 6, 0)
        self.layout.addWidget(self.coeff_c, 6, 1)
        self.layout.addWidget(self.conc_d_label, 7, 0)
        self.layout.addWidget(self.conc_d, 7, 1)
        self.layout.addWidget(self.coeff_d_label, 8, 0)
        self.layout.addWidget(self.coeff_d, 8, 1)
        self.layout.addWidget(self.equilibrium_constant_label, 9, 0)
        self.layout.addWidget(self.equilibrium_constant, 9, 1)

    def check_empty_input(self):
        empty_count = 0
        empty_input = None

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        for item in self.input_list:
            if item.text().strip() == "":
                empty_count += 1
                empty_input = item

        if empty_input in self.concentration_list and empty_count == 1 or self.calculated_value in self.concentration_list:
            self.calculate_concentration(empty_input)
        elif empty_input in self.coeff_list and empty_count == 1 or self.calculated_value in self.coeff_list:
            self.calculate_coefficient(empty_input)
        elif empty_input == self.equilibrium_constant and empty_count == 1 or self.calculated_value == self.equilibrium_constant:
            self.calculate_constant()
        else:
            show_dialog("")
            return

    def calculate_constant(self):
        try:
            k = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                    float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                        (float(self.conc_a.text()) ** float(self.coeff_a.text())) *
                        (float(self.conc_b.text()) ** float(self.coeff_b.text())))
        except OverflowError:
            print("Overflow Error, inputted numbers are too large")
            show_dialog("Overflow Error, inputted numbers are too large!")
            return
        self.calculated_value = self.equilibrium_constant
        self.update_gui(self.equilibrium_constant, k)

    def calculate_concentration(self, to_find):
        if to_find == self.conc_a or to_find == self.calculated_value:
            try:
                conc = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                        float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                               float(self.equilibrium_constant.text()) * (
                               float(self.conc_b.text()) ** float(self.coeff_b.text())))
                if float(self.coeff_a.text()) > 1:
                    conc = conc ** (1 / float(self.coeff_a.text()))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, conc)
            return

        if to_find == self.conc_b or to_find == self.calculated_value:
            try:
                conc = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                        float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                               float(self.equilibrium_constant.text()) * (
                               float(self.conc_a.text()) ** float(self.coeff_a.text())))
                if float(self.coeff_b.text()) > 1:
                    conc = conc ** (1 / float(self.coeff_b.text()))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, conc)
            return

        if to_find == self.conc_c or to_find == self.calculated_value:
            try:
                conc = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                        float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                            float(self.equilibrium_constant.text())) / (
                                float(self.conc_d.text()) ** float(self.coeff_d.text())))
                if float(self.coeff_c.text()) > 1:
                    conc = conc ** (1 / float(self.coeff_c.text()))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, conc)
            return

        if to_find == self.conc_d or to_find == self.calculated_value:
            try:
                conc = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                        float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                            float(self.equilibrium_constant.text())) / (
                                float(self.conc_c.text()) ** float(self.coeff_c.text())))
                if float(self.coeff_d.text()) > 1:
                    conc = conc ** (1 / float(self.coeff_d.text()))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.update_gui(to_find, conc)
            return

    def calculate_coefficient(self, to_find):
        if to_find == self.coeff_a or to_find == self.calculated_value:
            try:
                coeff = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                        float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                                float(self.equilibrium_constant.text()) * (
                                float(self.conc_b.text()) ** float(self.coeff_b.text())))
                coeff = int(log(coeff, float(self.conc_a.text())))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

        if to_find == self.coeff_b or to_find == self.calculated_value:
            try:
                coeff = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                        float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                                float(self.equilibrium_constant.text()) * (
                                float(self.conc_a.text()) ** float(self.coeff_a.text())))
                coeff = int(log(coeff, float(self.conc_b.text())))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

        if to_find == self.coeff_c or to_find == self.calculated_value:
            try:
                coeff = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                        float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                             float(self.equilibrium_constant.text())) / (
                                 float(self.conc_d.text()) ** float(self.coeff_d.text())))
                coeff = int(log(coeff, float(self.conc_c.text())))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

        if to_find == self.coeff_d or to_find == self.calculated_value:
            try:
                coeff = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                        float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                             float(self.equilibrium_constant.text())) / (
                                 float(self.conc_c.text()) ** float(self.coeff_c.text())))
                coeff = int(log(coeff, float(self.conc_d.text())))
            except OverflowError:
                print("Overflow Error, inputted numbers too large")
                show_dialog("Overflow Error, inputted numbers are too large!")
                return
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

    def update_gui(self, empty_input, value):
        if empty_input is self.calculated_value:
            empty_input.setText(str(value))


class GibbsFreeEnergyCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QGridLayout()

        self.temperature_conversions = {
            "°C": 273.15,
            "°K": 0.0,
        }

        self.general_energy_conversions = {
            "kJ": 1.0,
            "J": 0.001
        }

        self.gibbs_free_energy_label = QLabel("Gibbs Free Energy (ΔG):")
        self.enthalpy_change_label = QLabel("Enthalpy Change (ΔH):")
        self.temp_label = QLabel("Temperature:")
        self.entropy_change_label = QLabel("Entropy Change (ΔS):")

        self.gibbs_free_energy_input = QLineEdit()
        self.enthalpy_change_input = QLineEdit()
        self.temp_input = QLineEdit()
        self.entropy_change_input = QLineEdit()

        self.input_list = [self.gibbs_free_energy_input, self.entropy_change_input, self.temp_input,
                           self.enthalpy_change_input]

        self.gibbs_free_energy_unit_dropdown = QComboBox()
        self.gibbs_free_energy_unit_dropdown.addItem("kJ")
        self.gibbs_free_energy_unit_dropdown.addItem("J")

        self.gibbs_free_energy_unit_dropdown.setCurrentIndex(0)

        self.enthalpy_change_unit_dropdown = QComboBox()
        self.enthalpy_change_unit_dropdown.addItem("kJ")
        self.enthalpy_change_unit_dropdown.addItem("J")

        self.enthalpy_change_unit_dropdown.setCurrentIndex(0)

        self.temp_unit_dropdown = QComboBox()
        self.temp_unit_dropdown.addItem("°C")
        self.temp_unit_dropdown.addItem("°K")

        self.temp_unit_dropdown.setCurrentIndex(1)

        self.entropy_change_unit_dropdown = QComboBox()
        self.entropy_change_unit_dropdown.addItem("kJ")
        self.entropy_change_unit_dropdown.addItem("J")

        self.entropy_change_unit_dropdown.setCurrentIndex(1)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.perform_calculation)

        self.layout.addWidget(self.gibbs_free_energy_label, 0, 0)
        self.layout.addWidget(self.gibbs_free_energy_input, 0, 1)
        self.layout.addWidget(self.gibbs_free_energy_unit_dropdown, 0, 2)

        self.layout.addWidget(self.enthalpy_change_label, 1, 0)
        self.layout.addWidget(self.enthalpy_change_input, 1, 1)
        self.layout.addWidget(self.enthalpy_change_unit_dropdown, 1, 2)

        self.layout.addWidget(self.temp_label, 2, 0)
        self.layout.addWidget(self.temp_input, 2, 1)
        self.layout.addWidget(self.temp_unit_dropdown, 2, 2)

        self.layout.addWidget(self.entropy_change_label, 3, 0)
        self.layout.addWidget(self.entropy_change_input, 3, 1)
        self.layout.addWidget(self.entropy_change_unit_dropdown, 3, 2)

        self.layout.addWidget(self.calculate_button, 4, 0, 1, 3)

    def update_gibbs_free_energy(self, free_energy):
        self.gibbs_free_energy_input.setText(free_energy)

    def update_enthalpy_change(self, enthalpy_change):
        self.enthalpy_change_input.setText(enthalpy_change)

    def update_temperature(self, temp):
        self.temp_input.setText(temp)

    def update_entropy_change(self, entropy_change):
        self.entropy_change_input.setText(entropy_change)

    def perform_calculation(self):
        free_energy_unit = self.gibbs_free_energy_unit_dropdown.currentText()
        enthalpy_unit = self.enthalpy_change_unit_dropdown.currentText()
        temp_unit = self.temp_unit_dropdown.currentText()
        entropy_unit = self.entropy_change_unit_dropdown.currentText()

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        to_calc = find_empty_input(self.input_list.copy())

        if to_calc is self.gibbs_free_energy_input:
            free_energy = self.calculate_free_energy_change(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if free_energy:
                self.update_gibbs_free_energy(str(free_energy))
        elif to_calc is self.enthalpy_change_input:
            enthalpy_change = self.calculate_enthalpy_change(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if enthalpy_change:
                self.update_enthalpy_change(str(enthalpy_change))
        elif to_calc is self.temp_input:
            temperature = self.calculate_temperature(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if temperature:
                self.update_temperature(str(temperature))
        elif to_calc is self.entropy_change_input:
            entropy_change = self.calculate_entropy_change(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if entropy_change:
                self.update_entropy_change(str(entropy_change))

    def calculate_free_energy_change(self, free_energy_unit, enthalpy_unit, temp_unit, entropy_unit):
        try:
            free_energy = (float(self.enthalpy_change_input.text()) * self.general_energy_conversions[
                enthalpy_unit]) - ((float(self.temp_input.text()) + self.temperature_conversions[temp_unit]) * (
                    float(self.entropy_change_input.text()) * self.general_energy_conversions[entropy_unit]))
            free_energy = free_energy * self.general_energy_conversions[free_energy_unit]
            return free_energy
        except ValueError:
            print("Value Error")
            show_dialog("Value Error!")
            return

    def calculate_enthalpy_change(self, free_energy_unit, enthalpy_unit, temp_unit, entropy_unit):
        try:
            enthalpy_change = (float(self.gibbs_free_energy_input.text()) * self.general_energy_conversions[
                free_energy_unit]) + ((float(self.temp_input.text()) + self.temperature_conversions[temp_unit]) * (
                    float(self.entropy_change_input.text()) * self.general_energy_conversions[entropy_unit]))
            enthalpy_change = enthalpy_change * self.general_energy_conversions[enthalpy_unit]
            return enthalpy_change
        except ValueError:
            print("Value Error")
            show_dialog("Value Error!")
            return

    def calculate_temperature(self, free_energy_unit, enthalpy_unit, temp_unit, entropy_unit):
        try:
            temperature = ((float(self.enthalpy_change_input.text()) * self.general_energy_conversions[
                enthalpy_unit]) - (float(self.gibbs_free_energy_input.text()) * self.general_energy_conversions[
                free_energy_unit])) / (
                                  float(self.entropy_change_input.text()) * self.general_energy_conversions[
                              entropy_unit])
            temperature = temperature + self.temperature_conversions[temp_unit]
            return temperature
        except ValueError:
            print("Value Error")
            show_dialog("Value Error!")
            return

    def calculate_entropy_change(self, free_energy_unit, enthalpy_unit, temp_unit, entropy_unit):
        try:
            entropy_change = ((float(self.enthalpy_change_input.text()) * self.general_energy_conversions[
                enthalpy_unit]) - (float(self.gibbs_free_energy_input.text()) * self.general_energy_conversions[
                free_energy_unit])) / (
                                     float(self.temp_input.text()) + self.temperature_conversions[temp_unit])
            entropy_change = entropy_change / self.general_energy_conversions[entropy_unit]
            return entropy_change
        except ValueError:
            print("Value Error")
            show_dialog("Value Error!")
            return


class SpecificHeatCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.layout = QGridLayout()

        self.mass_conversions = {
            "mg": 0.001,
            "g": 1,
            "kg": 1000,
            "t": 1000000
        }

        self.temperature_conversions = {
            "°C": 273.15,
            "°K": 0.0,
        }

        self.energy_conversions = {
            "kJ": 0.001,
            "J": 1.0
        }

        self.energy_label = QLabel("Heat Energy: ")
        self.mass_label = QLabel("Mass: ")
        self.heat_capacity_label = QLabel("Specific Heat Capacity: ")
        self.temperature_change_label = QLabel("Temperature Change: ")

        self.energy_input = QLineEdit()
        self.mass_input = QLineEdit()
        self.heat_capacity_input = QLineEdit()
        self.temperature_change_input = QLineEdit()

        self.input_list = [self.energy_input, self.mass_input, self.heat_capacity_input, self.temperature_change_input]

        self.energy_unit_dropdown = QComboBox()
        self.energy_unit_dropdown.addItem("J")
        self.energy_unit_dropdown.addItem("kJ")

        self.energy_unit_dropdown.setCurrentIndex(0)

        self.mass_unit_dropdown = QComboBox()
        self.mass_unit_dropdown.addItem("mg")
        self.mass_unit_dropdown.addItem("g")
        self.mass_unit_dropdown.addItem("kg")

        self.mass_unit_dropdown.setCurrentIndex(1)

        self.temp_unit_dropdown = QComboBox()
        self.temp_unit_dropdown.addItem("°C")
        self.temp_unit_dropdown.addItem("°K")

        self.temp_unit_dropdown.setCurrentIndex(1)

        self.calculate_button = QPushButton("Calculate")

        self.calculate_button.clicked.connect(self.calculate)

        self.layout.addWidget(self.energy_label, 0, 0)
        self.layout.addWidget(self.energy_input, 0, 1)
        self.layout.addWidget(self.energy_unit_dropdown, 0, 2)

        self.layout.addWidget(self.mass_label, 1, 0)
        self.layout.addWidget(self.mass_input, 1, 1)
        self.layout.addWidget(self.mass_unit_dropdown, 1, 2)

        self.layout.addWidget(self.heat_capacity_label, 2, 0)
        self.layout.addWidget(self.heat_capacity_input, 2, 1)

        self.layout.addWidget(self.temperature_change_label, 3, 0)
        self.layout.addWidget(self.temperature_change_input, 3, 1)
        self.layout.addWidget(self.temp_unit_dropdown, 3, 2)

        self.layout.addWidget(self.calculate_button, 4, 1)

    def update_energy(self, energy):
        self.energy_input.setText(str(energy))

    def update_mass(self, mass):
        self.mass_input.setText(str(mass))

    def update_heat_capacity(self, hc):
        self.heat_capacity_input.setText(str(hc))

    def update_temp_change(self, temp):
        self.temperature_change_input.setText(str(temp))

    def calculate(self):
        energy_unit = self.energy_conversions[self.energy_unit_dropdown.currentText()]
        mass_unit = self.mass_conversions[self.mass_unit_dropdown.currentText()]
        temp_unit = self.temperature_conversions[self.temp_unit_dropdown.currentText()]

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        to_calc = find_empty_input(self.input_list.copy())

        if to_calc is self.energy_input:
            energy = self.__calculate_energy(energy_unit, mass_unit, temp_unit)
            if energy:
                self.update_energy(energy)
        if to_calc is self.mass_input:
            mass = self.__calculate_mass(energy_unit, mass_unit, temp_unit)
            if mass:
                self.update_mass(mass)
        if to_calc is self.heat_capacity_input:
            heat_capacity = self.__calculate_heat_capacity(energy_unit, mass_unit, temp_unit)
            if heat_capacity:
                self.update_heat_capacity(heat_capacity)
        if to_calc is self.temperature_change_input:
            temp = self.__calculate_temp_change(energy_unit, mass_unit, temp_unit)
            if temp:
                self.update_temp_change(temp)

    def __calculate_energy(self, energy_unit, mass_unit, temp_unit):
        try:
            q = (float(self.mass_input.text()) * mass_unit) * float(self.heat_capacity_input.text()) * (
                    float(self.temperature_change_input.text()) + temp_unit)
            q = q * energy_unit

            return q
        except ValueError:
            print("ValueError")
            return

    def __calculate_mass(self, energy_unit, mass_unit, temp_unit):
        try:
            mass = (float(self.energy_input.text()) * energy_unit) / (float(self.heat_capacity_input.text()) * (
                    float(self.temperature_change_input.text()) + temp_unit))
            mass = mass * mass_unit

            return mass
        except ValueError:
            print("ValueError")
            return

    def __calculate_heat_capacity(self, energy_unit, mass_unit, temp_unit):
        try:
            heat_capacity = (float(self.energy_input.text()) * energy_unit) / (
                    (float(self.mass_input.text()) * mass_unit) * (
                    float(self.temperature_change_input.text()) + temp_unit))

            return heat_capacity
        except ValueError:
            print("ValueError")
            return

    def __calculate_temp_change(self, energy_unit, mass_unit, temp_unit):
        try:
            temp_change = (float(self.energy_input.text()) * energy_unit) / (
                    (float(self.mass_input.text()) * mass_unit) * (
                float(self.heat_capacity_input.text())))
            temp_change = temp_change + temp_unit

            return temp_change
        except ValueError:
            print("ValueError")
            return


class RateCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()

        self.order_conversion = {
            "First": 1,
            "Second": 2
        }

        self.layout = QVBoxLayout()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        self.step_dropdown = QComboBox()
        self.step_dropdown.addItem("Unimolecular")
        self.step_dropdown.addItem("Bimolecular")
        self.step_dropdown.addItem("Trimolecular")
        self.step_dropdown.currentIndexChanged.connect(self.get_ui)

        self.layout.addWidget(self.step_dropdown)

        # Unimolecular Box
        self.unimol_box = RateBox("[A]")
        self.unimol_box_widget = QWidget()
        self.unimol_box_widget.setLayout(self.unimol_box.box_layout)

        self.unimol_conc_input = self.unimol_box.conc_input
        self.unimol_order_input = self.unimol_box.order_input

        self.unimol_order_input.currentTextChanged.connect(self.get_total_order)

        # Bimolecular Box
        self.bimol_box = RateBox("[B]")
        self.bimol_box_widget = QWidget()
        self.bimol_box_widget.setLayout(self.bimol_box.box_layout)

        self.bimol_conc_input = self.bimol_box.conc_input
        self.bimol_order_input = self.bimol_box.order_input

        self.bimol_order_input.currentTextChanged.connect(self.get_total_order)

        # Trimolecular Box
        self.trimol_box = RateBox("[C]")
        self.trimol_box_widget = QWidget()
        self.trimol_box_widget.setLayout(self.trimol_box.box_layout)

        self.trimol_conc_input = self.trimol_box.conc_input
        self.trimol_order_input = self.trimol_box.order_input

        self.trimol_order_input.currentTextChanged.connect(self.get_total_order)

        # Result Box
        self.result_box = RateResultBox()
        self.result_box_widget = QWidget()
        self.result_box_widget.setLayout(self.result_box.box_layout)

        self.rate_constant_input = self.result_box.rate_constant_input
        self.rate_input = self.result_box.rate_input
        self.total_order_input = self.result_box.total_order_input
        self.total_order_input.setReadOnly(True)

        # List containing every line edit currently visible on screen
        self.input_list = [self.unimol_conc_input, self.rate_constant_input, self.rate_input]
        self.conc_input_list = [self.unimol_conc_input, self.bimol_conc_input, self.trimol_conc_input]

        self.get_ui()

    def get_ui(self) -> None:
        """
        This method adds the necessary widgets to the current layout and makes sure that widgets are removed or added
        when needed.
        """

        self.update_input_list()
        self.get_total_order()

        self.layout.addWidget(self.unimol_box_widget)
        self.layout.addWidget(self.bimol_box_widget)
        self.layout.addWidget(self.trimol_box_widget)
        self.layout.addWidget(self.result_box_widget)
        self.layout.addWidget(self.calculate_button)

        # Hide the widgets to ensure correct order of display
        self.bimol_box_widget.hide()
        self.trimol_box_widget.hide()
        self.result_box_widget.hide()
        self.calculate_button.hide()

        if self.step_dropdown.currentIndex() == 1:
            self.bimol_box_widget.show()
            self.result_box_widget.show()
            self.calculate_button.show()
        elif self.step_dropdown.currentIndex() == 2:
            self.bimol_box_widget.show()
            self.trimol_box_widget.show()
            self.result_box_widget.show()
            self.calculate_button.show()
        else:
            self.result_box_widget.show()
            self.calculate_button.show()

    def update_input_list(self) -> None:
        """
        This function makes sure the self.input_list is always xup-to-date with the inputs displayed in the gui.
        """

        if self.bimol_conc_input in self.input_list.copy():
            self.input_list.remove(self.bimol_conc_input)
        if self.trimol_conc_input in self.input_list.copy():
            self.input_list.remove(self.trimol_conc_input)

        if self.step_dropdown.currentIndex() == 1:
            self.input_list.append(self.bimol_conc_input)
        elif self.step_dropdown.currentIndex() == 2:
            self.input_list.append(self.bimol_conc_input)
            self.input_list.append(self.trimol_conc_input)

    def calculate(self) -> None:
        """
        This method checks which input has been left empty, and then calls the according method to calculate the
        missing value.
        """

        if not find_empty_input(self.input_list.copy()):
            show_dialog("Must leave one input line empty for it to be calculated!")
            return
        elif check_invalid_symbol(self.input_list.copy()):
            show_dialog("Only numerical values in the form of integers or decimals allowed!")
            return

        unimol_order = self.order_conversion[self.unimol_order_input.currentText()]
        bimol_order = self.order_conversion[self.bimol_order_input.currentText()]
        trimol_order = self.order_conversion[self.trimol_order_input.currentText()]

        to_find = find_empty_input(self.input_list)

        if to_find is self.rate_input:
            self.calculate_rate(unimol_order, bimol_order, trimol_order)
        elif to_find is self.rate_constant_input:
            self.calculate_rate_constant(unimol_order, bimol_order, trimol_order)
        elif to_find in self.conc_input_list:
            self.calculate_concentration(to_find, unimol_order, bimol_order, trimol_order)

    def get_total_order(self) -> None:
        """
        This method makes sure the total order is always displayed correctly.
        """

        unimol_order = self.order_conversion[self.unimol_order_input.currentText()]
        bimol_order = self.order_conversion[self.bimol_order_input.currentText()]
        trimol_order = self.order_conversion[self.trimol_order_input.currentText()]

        total_order = unimol_order
        if self.step_dropdown.currentIndex() == 1:
            total_order += bimol_order
        elif self.step_dropdown.currentIndex() == 2:
            total_order += bimol_order + trimol_order

        self.update_total_order(total_order)

    def calculate_rate(self, unimol_order: int, bimol_order: int, trimol_order: int) -> None:
        """
        Calculates the rate of the reaction based on the elementary step
        (unimolecula, bimolecular, trimolecular), and then calls the update_input() method to display the calculated
        result.
        """

        rate = float(self.rate_constant_input.text()) * (float(self.unimol_conc_input.text()) ** unimol_order)

        if self.step_dropdown.currentIndex() == 1:
            rate = rate * (float(self.bimol_conc_input.text()) ** bimol_order)
        elif self.step_dropdown.currentIndex() == 2:
            rate = rate * (float(self.bimol_conc_input.text()) ** bimol_order) * (
                    float(self.trimol_conc_input.text()) ** trimol_order)

        self.update_input(rate)

    def calculate_rate_constant(self, unimol_order: int, bimol_order: int, trimol_order: int) -> None:
        """
        Calculates the rate constant based on the elementary step
        (unimolecula, bimolecular, trimolecular), and calls the update_input method to display the calculated result.
        """

        total_conc = (float(self.unimol_conc_input) ** unimol_order)

        if self.step_dropdown.currentIndex() == 1:
            total_conc = total_conc * (float(self.bimol_conc_input.text()) ** bimol_order)
        elif self.step_dropdown.currentIndex() == 2:
            total_conc = total_conc * (float(self.bimol_conc_input.text()) ** bimol_order) * (
                    float(self.trimol_conc_input.text()) ** trimol_order)

        rate_constant = float(self.rate_input) / total_conc

        self.update_input(rate_constant)

    def calculate_concentration(self, to_find: QLineEdit, unimol_order: int, bimol_order: int,
                                trimol_order: int) -> None:
        """
        Calculates the concentration of the given empty concentration input, based on the elementary step
        (unimolecula, bimolecular, trimolecular), and then calls the update_input() method to display the calculated
        result.
        """

        concentration = float(self.rate_input.text()) / float(self.rate_constant_input.text())

        if to_find is self.unimol_conc_input:
            if self.step_dropdown.currentIndex() == 1:
                concentration = concentration / (float(self.bimol_conc_input.text()) ** bimol_order)
            elif self.step_dropdown.currentIndex() == 2:
                concentration = concentration / ((float(self.bimol_conc_input.text()) ** bimol_order) * (
                        float(self.trimol_conc_input.text()) ** trimol_order))
            concentration = concentration ** (1 / unimol_order)
        elif to_find is self.bimol_conc_input:
            if self.step_dropdown.currentIndex() == 1:
                concentration = concentration / (float(self.unimol_conc_input.text()) ** unimol_order)
            elif self.step_dropdown.currentIndex() == 2:
                concentration = concentration / ((float(self.unimol_conc_input.text()) ** unimol_order) * (
                        float(self.trimol_conc_input.text()) ** trimol_order))
            concentration = concentration ** (1 / bimol_order)
        elif to_find is self.trimol_conc_input:
            concentration = concentration / (
                    (float(self.unimol_conc_input.text()) ** unimol_order) * (
                    float(self.bimol_conc_input.text()) ** bimol_order))
            concentration = concentration ** (1 / trimol_order)
        else:
            return
        self.update_input(concentration)

    def update_input(self, result: float) -> None:
        """
        Uses the find_empty_input() function to find the empty input, and then updates it using the result parameter.
        """

        find_empty_input(self.input_list.copy()).setText(str(result))

    def update_total_order(self, order: float) -> None:
        """
        Updates the total order input with the order parameter.
        """

        self.total_order_input.setText(str(order))
