from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QLabel, QComboBox, QVBoxLayout, QScrollArea, \
    QHBoxLayout

from math import log


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

        self.get_moles_layout()

    def moles_calculation(self):
        """
        This function performs all the calculation needed for the molesCalculation,
        and returns the value in the GUI.
        """

        mass_unit = self.mass_unit_dropdown.currentText()
        moles_unit = self.moles_unit_dropdown.currentText()

        if not self.moles_input.text().strip():
            try:
                moles = (float(self.mass_input.text()) * self.mass_conversions[mass_unit]) / float(self.mr_input.text())
                self.update_moles_calculation(moles)
                self.moles_unit_dropdown.setCurrentText("mol")
            except ValueError:
                print("Value Error")
        elif not self.mass_input.text().strip():
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
        self.conc_layout = QGridLayout()

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

        self.get_conc_layout()

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

        moles_unit = self.moles_unit_dropdown_conc.currentText()
        vol_unit = self.vol_unit_drop_down_conc.currentText()

        if not self.conc_input_conc.text():
            try:
                conc = (float(self.moles_input_conc.text()) * self.mole_conversions[moles_unit]) / (
                        float(self.vol_input_conc.text()) * self.volume_conversions[vol_unit])
                self.conc_input_conc.setText(str(conc))
            except ValueError:
                print("Value Error")
        elif not self.moles_input_conc.text():
            try:
                moles = float(self.conc_input_conc.text()) * (
                        float(self.vol_input_conc.text()) * self.volume_conversions[vol_unit])
                (self.moles_input_conc.setText(str(moles)))
            except ValueError:
                print("Value Error")
        else:
            try:
                vol = (float(self.moles_input_conc.text()) * self.mole_conversions[moles_unit]) / float(
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


class AvogadroCalculator(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
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

        # Initialise Atom Economy calculator

        self.get_avogadro_layout()

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


class IdealGasLawCalculator(QWidget):
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
                    self.temperature_input_igl.text()) + self.temperature_conversions[temperature_unit])) / (
                                   float(self.volume_input_igl.text()) * self.volume_conversions[volume_unit])
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

        if not self.pressure_input_igl.text().strip():
            self.pressure_input_igl.setText(str(_calculate_pressure()))
        elif not self.volume_input_igl.text().strip():
            self.volume_input_igl.setText(str(_calculate_volume()))
        elif not self.temperature_input_igl.text().strip():
            self.temperature_input_igl.setText(str(_calculate_temperature()))
        elif not self.moles_input_igl.text().strip():
            self.moles_input_igl.setText(str(_calculate_moles()))


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
            return "Invalid Input Error"

    def calculate_constant(self):
        try:
            k = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                    float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                        (float(self.conc_a.text()) ** float(self.coeff_a.text())) *
                        (float(self.conc_b.text()) ** float(self.coeff_b.text())))
        except OverflowError:
            print("Overflow Error, inputted numbers too big")
            return
        self.calculated_value = self.equilibrium_constant
        self.update_gui(self.equilibrium_constant, k)

    def calculate_concentration(self, to_find):
        if to_find == self.conc_a or to_find == self.calculated_value:
            conc = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                    float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                           float(self.equilibrium_constant.text()) * (
                           float(self.conc_b.text()) ** float(self.coeff_b.text())))
            if float(self.coeff_a.text()) > 1:
                conc = conc ** (1 / float(self.coeff_a.text()))
            self.calculated_value = to_find
            self.update_gui(to_find, conc)
            return

        if to_find == self.conc_b or to_find == self.calculated_value:
            conc = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                    float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                           float(self.equilibrium_constant.text()) * (
                           float(self.conc_a.text()) ** float(self.coeff_a.text())))
            if float(self.coeff_b.text()) > 1:
                conc = conc ** (1 / float(self.coeff_b.text()))
            self.calculated_value = to_find
            self.update_gui(to_find, conc)
            return

        if to_find == self.conc_c or to_find == self.calculated_value:
            conc = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                    float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                        float(self.equilibrium_constant.text())) / (
                            float(self.conc_d.text()) ** float(self.coeff_d.text())))
            if float(self.coeff_c.text()) > 1:
                conc = conc ** (1 / float(self.coeff_c.text()))
            self.calculated_value = to_find
            self.update_gui(to_find, conc)
            return

        if to_find == self.conc_d or to_find == self.calculated_value:
            conc = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                    float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                        float(self.equilibrium_constant.text())) / (
                            float(self.conc_c.text()) ** float(self.coeff_c.text())))
            if float(self.coeff_d.text()) > 1:
                conc = conc ** (1 / float(self.coeff_d.text()))
            self.update_gui(to_find, conc)
            return

    def calculate_coefficient(self, to_find):
        if to_find == self.coeff_a or to_find == self.calculated_value:
            coeff = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                    float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                            float(self.equilibrium_constant.text()) * (
                            float(self.conc_b.text()) ** float(self.coeff_b.text())))
            coeff = int(log(coeff, float(self.conc_a.text())))
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

        if to_find == self.coeff_b or to_find == self.calculated_value:
            coeff = ((float(self.conc_c.text()) ** float(self.coeff_c.text())) * (
                    float(self.conc_d.text()) ** float(self.coeff_d.text()))) / (
                            float(self.equilibrium_constant.text()) * (
                            float(self.conc_a.text()) ** float(self.coeff_a.text())))
            coeff = int(log(coeff, float(self.conc_b.text())))
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

        if to_find == self.coeff_c or to_find == self.calculated_value:
            coeff = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                    float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                         float(self.equilibrium_constant.text())) / (
                             float(self.conc_d.text()) ** float(self.coeff_d.text())))
            coeff = int(log(coeff, float(self.conc_c.text())))
            self.calculated_value = to_find
            self.update_gui(to_find, coeff)
            return

        if to_find == self.coeff_d or to_find == self.calculated_value:
            coeff = ((float(self.conc_a.text()) ** float(self.coeff_a.text())) * (
                    float(self.conc_b.text()) ** float(self.coeff_b.text())) * (
                         float(self.equilibrium_constant.text())) / (
                             float(self.conc_c.text()) ** float(self.coeff_c.text())))
            coeff = int(log(coeff, float(self.conc_d.text())))
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

        if self.gibbs_free_energy_input.text().strip() == "":
            free_energy = self.calculate_free_energy_change(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if free_energy:
                self.update_gibbs_free_energy(str(free_energy))
        elif self.enthalpy_change_input.text().strip() == "":
            enthalpy_change = self.calculate_enthalpy_change(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if enthalpy_change:
                self.update_enthalpy_change(str(enthalpy_change))
        elif self.temp_input.text().strip() == "":
            temperature = self.calculate_temperature(free_energy_unit, enthalpy_unit, temp_unit, entropy_unit)
            if temperature:
                self.update_temperature(str(temperature))
        elif self.entropy_change_input.text().strip() == "":
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
            return

    def calculate_temperature(self, free_energy_unit, enthalpy_unit, temp_unit, entropy_unit):
        try:
            temperature = ((float(self.enthalpy_change_input.text()) * self.general_energy_conversions[
                enthalpy_unit]) - (float(self.gibbs_free_energy_input.text()) * self.general_energy_conversions[
                free_energy_unit])) / (
                                  float(self.entropy_change_input.text()) * self.general_energy_conversions[entropy_unit])
            temperature = temperature + self.temperature_conversions[temp_unit]
            return temperature
        except ValueError:
            print("Value Error")
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
            return
