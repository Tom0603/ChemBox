import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QGridLayout, QWidget, QPushButton, \
    QLineEdit, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem

import re
from sympy import Matrix, lcm

from chem_editor_gui import ChemEditor


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

        self.tab_bar = TabBar()
        self.setCentralWidget(self.tab_bar)

        self.side_bar = SideBar()

        self.tab_bar.tab1.setLayout(self.side_bar.main_layout)

        self.amount_of_substance = AmountOfSubstance()

        # Initialise moles tab in sidebar
        self.side_bar.moles_tab.setLayout(self.amount_of_substance.moles_layout)

        # Initialise concentration tab in sidebar
        self.side_bar.conc_tab.setLayout(self.amount_of_substance.conc_layout)

        # Initialise avogadro's calculator tab in sidebar
        self.side_bar.avogadro_tab.setLayout(self.amount_of_substance.avogadro_layout)

        # Initialise igl tab in sidebar
        self.ideal_gas_law = IdealGasLaw()
        self.side_bar.ideal_gas_tab.setLayout(self.ideal_gas_law.ideal_gas_layout)

        self.chem_balancer = ChemBalancer()
        self.tab_bar.tab3.setLayout(self.chem_balancer.balancer_layout)

        self.chem_editor = ChemEditor()
        self.tab_bar.tab5.setLayout(self.chem_editor.editor_layout)

        # self.interactiveTable = InteractiveTable()
        # self.tabBar.tab2.setLayout(self.interactiveTable.tableLayout)


class AmountOfSubstance(QWidget):
    """
    This class holds all the calculations concerning the amount of a substance.
    Examples of this are the standard calculation n=m/mr or the c=n/v equation.
    """

    def __init__(self):
        super(QWidget, self).__init__()
        self.moles_layout = QGridLayout()
        self.conc_layout = QGridLayout()
        self.avogadro_layout = QGridLayout()

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

        # Initialise moles calculation Layout
        self.moles_label = QLabel("Moles:")
        self.mass_label = QLabel("Mass:")
        self.mr_label = QLabel("Molecular weight:")

        self.moles_input = QLineEdit()
        self.mass_input = QLineEdit()
        self.mr_input = QLineEdit()

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.moles_calculation)

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

        # Initialise concentration calculation Layout
        self.conc_label_conc = QLabel("Concentration:")
        self.moles_label_conc = QLabel("Moles:")
        self.vol_label_conc = QLabel("Volume:")

        self.conc_input_conc = QLineEdit()
        self.moles_input_conc = QLineEdit()
        self.vol_input_conc = QLineEdit()

        self.calculate_button_conc = QPushButton("Calculate")
        self.calculate_button_conc.clicked.connect(self.conc_calculation)

        self.moles_unit_dropdown_conc = QComboBox()
        self.moles_unit_dropdown_conc.addItem("μmol")
        self.moles_unit_dropdown_conc.addItem("mmol")
        self.moles_unit_dropdown_conc.addItem("mol")

        self.moles_unit_dropdown_conc.setCurrentIndex(2)

        self.vol_unit_drop_down_conc = QComboBox()
        self.vol_unit_drop_down_conc.addItem("cm³")
        self.vol_unit_drop_down_conc.addItem("dm³")
        self.vol_unit_drop_down_conc.addItem("m³")

        self.vol_unit_drop_down_conc.setCurrentIndex(1)

        # Initialise Avogadro's calculator
        self.mass_label_avogadro = QLabel("Mass:")
        self.moles_label_avogadro = QLabel("Moles:")
        self.molecular_weight_label_avogadro = QLabel("Molecular weight:")
        self.num_atoms_label_avogadro = QLabel("Number of atoms:")

        self.mass_input_avogadro = QLineEdit()
        self.moles_input_avogadro = QLineEdit()
        self.molecular_weight_input_avogadro = QLineEdit()
        self.num_atoms_input_avogadro = QLineEdit()

        self.calculate_button_avogadro = QPushButton("Calculate")
        self.calculate_button_avogadro.clicked.connect(self.calculate_avogadro)

        self.mass_unit_dropdown_avo = QComboBox()
        self.mass_unit_dropdown_avo.addItem("mg")
        self.mass_unit_dropdown_avo.addItem("g")
        self.mass_unit_dropdown_avo.addItem("kg")
        self.mass_unit_dropdown_avo.addItem("t")

        self.mass_unit_dropdown_avo.setCurrentIndex(1)

        self.get_moles_layout()
        self.get_conc_layout()
        self.get_avogadro_layout()

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

    def moles_calculation(self):
        """
        This function performs all the calculation needed for the molesCalculation,
        and returns the value in the GUI.
        """

        mass_unit = self.mass_unit_dropdown.currentText()
        moles_unit = self.moles_unit_dropdown.currentText()

        if not self.moles_input.text():
            try:
                moles = (float(self.mass_input.text()) * self.mass_conversions[mass_unit]) / float(self.mr_input.text())
                self.update_moles_calculation(moles)
                self.moles_unit_dropdown.setCurrentText("mol")
            except ValueError:
                print("Value Error")
        elif not self.mass_input.text():
            try:
                mass = (float(self.moles_input.text()) * self.mole_conversions[moles_unit]) * float(
                    self.mr_input.text())
                self.update_moles_calculation(mass)
            except ValueError:
                print("Value Error")
        else:
            try:
                mr = (float(self.mass_input.text()) * self.mass_conversions[mass_unit]) / (
                        float(self.moles_input.text()) * self.mole_conversions[moles_unit])
                self.update_moles_calculation(mr)
            except ValueError:
                print("Value Error")

    def update_moles_calculation(self, result):
        if not self.moles_input.text():
            self.moles_input.setText(str(result))
        elif not self.mass_input.text():
            self.mass_input.setText(str(result))
        else:
            self.mr_input.setText(str(result))

    def get_conc_layout(self):
        f"""
        This function adds all the essential widgets to the {self.conc_layout} 
        """

        self.conc_layout.addWidget(self.conc_label_conc, 0, 0)
        self.conc_layout.addWidget(self.moles_label_conc, 1, 0)
        self.conc_layout.addWidget(self.vol_label_conc, 2, 0)

        self.conc_layout.addWidget(self.conc_input_conc, 0, 1)
        self.conc_layout.addWidget(self.moles_input_conc, 1, 1)
        self.conc_layout.addWidget(self.vol_input_conc, 2, 1)

        self.conc_layout.addWidget(self.moles_unit_dropdown_conc, 1, 2)
        self.conc_layout.addWidget(self.vol_unit_drop_down_conc, 2, 2)

        self.conc_layout.addWidget(self.calculate_button_conc, 3, 1)

    def conc_calculation(self):
        """
        This function performs all the calculation needed for the concentration calculation,
        and returns the value in the GUI.
        """

        moles_unit = self.moles_unit_dropdown.currentText()
        vol_unit = self.vol_unit_drop_down_conc.currentText()

        if not self.conc_input_conc.text():
            try:
                conc = (float(self.moles_input.text()) * self.mole_conversions[moles_unit]) / (
                        float(self.vol_input_conc.text()) * self.volume_conversions[vol_unit])
                self.conc_input_conc.setText(str(conc))
            except ValueError:
                print("Value Error")
        elif not self.moles_input.text():
            try:
                moles = float(self.conc_input_conc.text()) * (
                        float(self.vol_input_conc.text()) * self.volume_conversions[vol_unit])
                self.mass_input.setText(str(moles))
            except ValueError:
                print("Value Error")
        else:
            try:
                vol = (float(self.moles_input.text()) * self.mole_conversions[moles_unit]) / float(
                    self.conc_input_conc.text())
                self.vol_input_conc.setText(str(vol))
            except ValueError:
                print("Value Error")

    def update_conc_calculation(self, result):
        if not self.conc_input_conc:
            self.conc_input_conc.setText(str(result))
        elif not self.moles_input_conc:
            self.moles_input_conc.setText(str(result))
        else:
            self.vol_input_conc.setText(str(result))

    def get_avogadro_layout(self):
        f"""
        This function adds all the essential widgets to the {self.avogadro_layout} 
        """

        self.avogadro_layout.addWidget(self.mass_label_avogadro, 0, 0)
        self.avogadro_layout.addWidget(self.moles_label_avogadro, 1, 0)
        self.avogadro_layout.addWidget(self.molecular_weight_label_avogadro, 2, 0)
        self.avogadro_layout.addWidget(self.num_atoms_label_avogadro, 3, 0)

        self.avogadro_layout.addWidget(self.mass_input_avogadro, 0, 1)
        self.avogadro_layout.addWidget(self.moles_input_avogadro, 1, 1)
        self.avogadro_layout.addWidget(self.molecular_weight_input_avogadro, 2, 1)
        self.avogadro_layout.addWidget(self.num_atoms_input_avogadro, 3, 1)

        self.avogadro_layout.addWidget(self.mass_unit_dropdown_avo, 0, 2)

        self.avogadro_layout.addWidget(self.calculate_button_avogadro, 4, 1)

    def calculate_avogadro(self):
        mass_unit = self.mass_unit_dropdown_avo.currentText()

        def _calculate_mass():
            mass = float(self.moles_input_avogadro.text()) * float(self.molecular_weight_input_avogadro.text())
            return mass

        def _calculate_moles():
            try:
                moles = float(self.num_atoms_input_avogadro.text()) / self.avogadros_constant
            except ValueError:
                try:
                    moles = (float(self.mass_input_avogadro.text()) * self.mass_conversions[mass_unit]) / float(
                        self.molecular_weight_input_avogadro.text())
                    return moles
                except ValueError:
                    return ""
            return moles

        def _calculate_mol_weight():
            mol_weight = (float(self.mass_input_avogadro.text()) * self.mass_conversions[mass_unit]) / float(
                self.moles_input_avogadro.text())
            return mol_weight

        def _calculate_num_atoms():
            num_atoms = float(self.moles_input_avogadro.text()) * self.avogadros_constant
            return num_atoms

        def _run_calculations():
            try:
                if not self.mass_input_avogadro.text():
                    self.update_mass_avogadro(str(_calculate_mass()))
            except ValueError:
                pass
            try:
                if not self.moles_input_avogadro.text():
                    self.moles_input_avogadro.setText(str(_calculate_moles()))
            except ValueError:
                pass
            try:
                if not self.molecular_weight_input_avogadro.text():
                    self.update_mol_weight_avogadro(str(_calculate_mol_weight()))
            except ValueError:
                pass
            try:
                if not self.num_atoms_input_avogadro.text():
                    self.update_num_atoms_avogadro(str(_calculate_num_atoms()))
            except ValueError:
                pass

        _run_calculations()

    def update_mass_avogadro(self, mass):
        self.mass_input_avogadro.setText(mass)

    def update_moles_avogadro(self, moles):
        self.moles_input_avogadro.setText(moles)

    def update_mol_weight_avogadro(self, mol_weight):
        self.molecular_weight_input_avogadro.setText(mol_weight)

    def update_num_atoms_avogadro(self, num_atoms):
        self.num_atoms_input_avogadro.setText(num_atoms)


class IdealGasLaw(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.ideal_gas_layout = QGridLayout()

        # Initialise Ideal Gas Law (IGL) properties
        self.ideal_gas_constant = 8.314

        self.pressure_input_igl = QLineEdit()
        self.volume_input_igl = QLineEdit()
        self.temperature_input_igl = QLineEdit()
        self.moles_input_igl = QLineEdit()

        self.pressure_label_igl = QLabel("Pressure:")
        self.volume_label_igl = QLabel("Volume:")
        self.temperature_label_igl = QLabel("Temperature:")
        self.moles_label_igl = QLabel("Amount of substance - moles:")
        self.calculate_button_igl = QPushButton('Calculate')
        self.result_label_igl = QLabel('Result will appear here')

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
        self.ideal_gas_layout.addWidget(self.pressure_input_igl, 0, 1)
        self.ideal_gas_layout.addWidget(self.pressure_drop_down_igl, 0, 2)

        self.ideal_gas_layout.addWidget(self.volume_label_igl, 1, 0)
        self.ideal_gas_layout.addWidget(self.volume_input_igl, 1, 1)
        self.ideal_gas_layout.addWidget(self.volume_drop_down_igl, 1, 2)

        self.ideal_gas_layout.addWidget(self.temperature_label_igl, 2, 0)
        self.ideal_gas_layout.addWidget(self.temperature_input_igl, 2, 1)
        self.ideal_gas_layout.addWidget(self.temperature_drop_down_igl, 2, 2)

        self.ideal_gas_layout.addWidget(self.moles_label_igl, 3, 0)
        self.ideal_gas_layout.addWidget(self.moles_input_igl, 3, 1)
        self.ideal_gas_layout.addWidget(self.calculate_button_igl, 4, 0)
        self.ideal_gas_layout.addWidget(self.result_label_igl, 4, 1)

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

        def _calculate_pressure():
            try:
                pressure = (float(self.moles_input_igl.text()) * self.ideal_gas_constant * (float(
                    self.temperature_input_igl.text()) + self.temperature_conversions[temperature_unit])) / (float(
                    self.volume_input_igl.text()) * self.volume_conversions[volume_unit])
                return pressure
            except ValueError:
                return "Value Error"

        def _calculate_volume():
            try:
                volume = (float(self.moles_input_igl.text()) * self.ideal_gas_constant * (float(
                    self.temperature_input_igl.text()) + self.temperature_conversions[temperature_unit])) / (
                                 float(self.pressure_input_igl.text()) * self.pressure_conversions[pressure_unit])
                return volume
            except ValueError:
                return "Value Error"

        def _calculate_temperature():
            try:
                temperature = ((float(self.pressure_input_igl.text()) * self.pressure_conversions[pressure_unit]) * (
                        float(
                            self.volume_input_igl.text()) * self.volume_conversions[volume_unit])) / (
                                      float(self.moles_input_igl.text()) * self.ideal_gas_constant)
                return temperature
            except ValueError:
                return "Value Error"

        def _calculate_moles():
            try:
                moles = ((float(self.pressure_input_igl.text()) * self.pressure_conversions[pressure_unit]) * (
                        float(self.volume_input_igl.text()) * self.volume_conversions[volume_unit])) / (
                                self.ideal_gas_constant * (float(self.temperature_input_igl.text()) +
                                                           self.temperature_conversions[temperature_unit]))
                return moles
            except ValueError:
                return "Value Error"

        if self.pressure_input_igl.text() == "":
            self.result_label_igl.setText(f"Pressure: {_calculate_pressure()}")
        elif self.volume_input_igl.text() == "":
            self.result_label_igl.setText(f"Volume: {_calculate_volume()}")
        elif self.temperature_input_igl.text() == "":
            self.result_label_igl.setText(f"Temperature: {_calculate_temperature()}")
        elif self.moles_input_igl.text() == "":
            self.result_label_igl.setText(f"Number of moles: {_calculate_moles()}")
        else:
            self.result_label_igl.setText("wtf are you doing mate")


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
        self.balancer_layout = QVBoxLayout()

        self.equation_input = QLineEdit()
        self.balance_button = QPushButton("Balance")
        self.balanced_label = QLabel()

        # Add the widgets to the balancerLayout
        self.balancer_layout.addWidget(self.equation_input)
        self.balancer_layout.addWidget(self.balance_button)
        self.balancer_layout.addWidget(self.balanced_label)

        self.balance_button.clicked.connect(self.run_balancer)

        self.stripped_equation = str()
        self.equation_split = list()

        self.reactants = list()
        self.products = list()

        self.element_list = list()
        self.element_matrix = list()

        self.balanced_equation = str()

    def clear_variables(self):
        """
        Clears all the used variables to avoid using data or values from previous calculations.
        """

        if len(self.equation_split) != 0:
            self.equation_split.clear()
        if len(self.reactants) != 0:
            self.reactants.clear()
        if len(self.products) != 0:
            self.products.clear()
        if len(self.element_list) != 0:
            self.element_list.clear()
        if len(self.element_matrix) != 0:
            self.element_matrix = []

        self.reactants = ""
        self.products = ""
        self.balanced_equation = ""

    def split_equation(self):
        f"""
        Takes {self.equation_input}, strips it from all the whitespaces
        and splits it up into separate reactants and products.
        """

        # Strip equation from any whitespaces
        try:
            self.stripped_equation = "".join(self.equation_input.text().split())
        except IndexError:
            return None
        print(self.stripped_equation)

        # Split equation into reactants (self.equationSplit[0]) and products (self.equationSplit[1])
        self.equation_split = self.stripped_equation.split("=")
        print(self.equation_split)

        try:
            self.reactants = self.equation_split[0].split("+")
        except IndexError:
            return None
        print(self.reactants)
        try:
            self.products = self.equation_split[1].split("+")
        except IndexError:
            return None
        print(self.products)

    def find_reagents(self, compound, index, side):
        f"""
        This Function finds separate reagents by removing brackets from the compounds
        and then calls {self.find_elements}.

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
                bracket_subscript = reagent.split(")", 1)[-1]
                if bracket_subscript:
                    bracket_subscript = int(bracket_subscript)
                else:
                    bracket_subscript = 1
                # Recursively find elements within the inner compound
                self.find_elements(inner_compound, index, bracket_subscript, side)
            else:
                # No brackets, directly find elements
                bracket_subscript = 1
                self.find_elements(reagent, index, bracket_subscript, side)

    def find_elements(self, reagent, index, bracket_subscript, side):
        f"""
        Separates out elements and subscripts using a regex,
        then loops through the elements and calls {self.add_to_matrix}.

        :param reagent: String of reagent (e.g. H2O).
        :param index: Index position of row in matrix.
        :param bracket_subscript: The subscript value outside the brackets. Equal to 1 if there are no brackets.
        :param side: "1" for reactants, "-1" for products.
        """

        # Use regex to separate elements and subscripts
        element_counts = re.findall("([A-Z][a-z]*)([0-9]*)", reagent)
        for element, subscript in element_counts:
            if not subscript:
                subscript = 1
            else:
                subscript = int(subscript)
            # Call addToMatrix for each element
            self.add_to_matrix(element, index, bracket_subscript * subscript, side)

    def add_to_matrix(self, element, index, count, side):
        """
        This function adds the provided element with a specified count to the matrix at the given index.
        The 'side' parameter determines whether the element is part of the reactants (positive side)
        or products (negative side) in the chemical equation.

        :param element: The element symbol as in the periodic table (e.g. Na).
        :param index: Index position of row in matrix.
        :param count: Number of specific element to add to the matrix.
        :param side: "1" for reactants, "-1" for products.
        """
        print(element, index, count, side)
        if index == len(self.element_matrix):
            print(self.element_matrix)
            self.element_matrix.append([])
            print(self.element_matrix)
            for x in self.element_list:
                print(self.element_list)
                self.element_matrix[index].append(0)
                print(self.element_matrix)

        if element not in self.element_list:
            self.element_list.append(element)
            for i in range(len(self.element_matrix)):
                self.element_matrix[i].append(0)
                print(self.element_matrix)

        column = self.element_list.index(element)
        self.element_matrix[index][column] += count * side
        print(self.element_list)
        print(self.element_matrix)

    def run_balancer(self):
        f"""
        This the core function of the {ChemBalancer} class,
        responsible for balancing chemical equations.
        It parses the user-provided equation, deciphers compounds,
        constructs a matrix, finds the null space for balancing coefficients,
        and computes the balanced equation.
        This function leverages SymPy for mathematical operations, ensuring accurate chemical equation balancing.
        """

        # Clear variables, in case the program was run before
        self.clear_variables()

        self.split_equation()

        for i in range(len(self.reactants)):
            self.find_reagents(self.reactants[i], i, 1)
        for i in range(len(self.products)):
            self.find_reagents(self.products[i], i + len(self.reactants), -1)

        self.element_matrix = Matrix(self.element_matrix)
        self.element_matrix = self.element_matrix.transpose()
        try:
            num = self.element_matrix.nullspace()[0]
        except IndexError:
            return None
        print(num)
        multiple = lcm([val.q for val in num])
        num = multiple * num
        print(num)

        coefficient = num.tolist()

        for i in range(len(self.reactants)):
            if coefficient[i][0] != 1:
                self.balanced_equation += str(coefficient[i][0]) + self.reactants[i]
            else:
                self.balanced_equation += self.reactants[i]
            if i < len(self.reactants) - 1:
                self.balanced_equation += " + "
        self.balanced_equation += " = "

        for i in range(len(self.products)):
            if coefficient[i + len(self.reactants)][0] != 1:
                self.balanced_equation += str(coefficient[i + len(self.reactants)][0]) + self.products[i]
            else:
                self.balanced_equation += self.products[i]
            if i < len(self.products) - 1:
                self.balanced_equation += " + "
        self.equation_input.setText(f"{self.balanced_equation}")


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


class InteractiveTable(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.table_layout = QVBoxLayout(self)

        self.table = QTableWidget()
        self.table_layout.addWidget(self.table)

        self.add_row_button = QPushButton("Add Row")
        self.delete_row_button = QPushButton("Delete Row")
        self.add_col_button = QPushButton("Add Column")
        self.delete_col_button = QPushButton("Delete Column")

        self.table_layout.addWidget(self.add_row_button)
        self.table_layout.addWidget(self.delete_row_button)
        self.table_layout.addWidget(self.add_col_button)
        self.table_layout.addWidget(self.delete_col_button)

        self.add_row_button.clicked.connect(self.add_row)
        self.delete_row_button.clicked.connect(self.del_row)
        self.add_col_button.clicked.connect(self.add_col)
        self.delete_col_button.clicked.connect(self.del_col)

        self.table.setRowCount(3)
        self.table.setColumnCount(3)
        self.create_table()

    def create_table(self):
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = QTableWidgetItem(f"Row {row}, Col {col}")
                self.table.setItem(row, col, item)

    def add_row(self):
        current_rows = self.table.rowCount()
        self.table.setRowCount(current_rows + 1)

    def add_col(self):
        current_cols = self.table.columnCount()
        self.table.setColumnCount(current_cols + 1)

    def del_row(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            self.table.removeRow(selected_row)

    def del_col(self):
        selected_col = self.table.currentColumn()
        if selected_col >= 0:
            self.table.removeColumn(selected_col)


def main():
    app = QApplication(sys.argv)

    # Load CSS file
    app.setStyleSheet(open('style.css').read())
    main_win = ChemBox()
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
