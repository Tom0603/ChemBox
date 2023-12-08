from PyQt6.QtWidgets import QApplication, QMainWindow, QTabWidget, QGridLayout, QWidget, QPushButton, \
    QLineEdit, QLabel, QComboBox, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem

import re
from sympy import Matrix, lcm


class ChemBalancer(QWidget):
    f"""
    This module is responsible for balancing chemical equations.
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