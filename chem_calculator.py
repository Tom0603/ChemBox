from PyQt6.QtWidgets import QGridLayout, QWidget, QPushButton, QLineEdit, QLabel, QComboBox


class MolesCalculator(QWidget):
    def __init__(self):
        super(QWidget).__init__()
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
        super(QWidget).__init__()
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


class AtomEconCalculator(QWidget):
    def __init__(self):
        super().__init__()

        self.atom_econ_layout = QGridLayout()
        self.reagent_list = []

        self.first_reagent_label = QLabel("Reagent 1")
        self.desired_product_label = QLabel("Desired Product")
        self.atom_economy_label = QLabel("Atom Economy")

        self.first_reagent = QLineEdit()
        self.reagent_list.append(self.first_reagent)

        self.desired_product = QLineEdit()
        self.atom_economy = QLineEdit()

        self.add_reagent_button = QPushButton("Add Reagent", self)
        self.add_reagent_button.clicked.connect(self.add_reagent)

        self.calculate_button = QPushButton("Calculate")
        self.calculate_button.clicked.connect(self.calculate)

        self.atom_econ_layout.addWidget(self.first_reagent_label, 0, 0)
        self.atom_econ_layout.addWidget(self.first_reagent, 0, 1)
        self.atom_econ_layout.addWidget(self.desired_product_label, 1, 0)
        self.atom_econ_layout.addWidget(self.desired_product, 1, 1)
        self.atom_econ_layout.addWidget(self.atom_economy_label, 2, 0)
        self.atom_econ_layout.addWidget(self.atom_economy, 2, 1)
        self.atom_econ_layout.addWidget(self.add_reagent_button, 3, 0)
        self.atom_econ_layout.addWidget(self.calculate_button, 3, 1)

    def add_reagent(self):
        new_reagent = QLineEdit()
        new_label = QLabel(f"Reagent {len(self.reagent_list) + 1}")
        self.reagent_list.append(new_reagent)
        self.atom_econ_layout.addWidget(new_label)
        self.atom_econ_layout.addWidget(new_reagent)

    def get_reagents(self):
        total = 0.0
        for reagent in self.reagent_list:
            try:
                total += float(reagent.text())
            except ValueError:
                continue
        return total

    def calculate_atom_econ(self):
        try:
            atom_economy = (float(self.desired_product.text()) / self.get_reagents()) * 100
        except ValueError:
            return "ValueError you twat"
        return atom_economy

    def calculate_desired_product(self):
        try:
            desired_product = (self.get_reagents() * float(self.atom_economy.text())) / 100
        except ValueError:
            return "ValueError you twat"
        return desired_product

    def calculate_reagent(self):
        try:
            reagent = ((float(self.desired_product.text()) / float(
                self.atom_economy.text())) - self.get_reagents()) * 100
        except ValueError:
            return "ValueError you twat"
        return reagent

    def calculate(self):
        if not self.first_reagent.text():
            reagent = self.calculate_reagent()
            self.update_ui(reagent)
        elif not self.desired_product.text():
            desired_product = self.calculate_desired_product()
            self.update_ui(desired_product)
        elif not self.atom_economy.text():
            atom_economy = self.calculate_atom_econ()
            self.update_ui(atom_economy)
        else:
            return ValueError

    def update_ui(self, result):
        if not self.first_reagent.text():
            try:
                self.first_reagent.setText(str(result))
            except ValueError:
                return
        elif not self.desired_product.text():
            try:
                self.desired_product.setText(str(result))
            except ValueError:
                return
        elif not self.atom_economy.text():
            try:
                self.atom_economy.setText(str(result))
            except ValueError:
                return
        else:
            return ValueError
