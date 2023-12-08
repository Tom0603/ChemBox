from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QLabel, QComboBox


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

        # Initialise Atom Economy calculator

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