from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen, QColor, QFont, QPalette, QBrush

import chem_editor_logic


class ChemEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.editor_layout = QGridLayout()
        self.setLayout(self.editor_layout)

        self.carbon_button = QPushButton("C")
        self.hydrogen_button = QPushButton("H")

        self.bond_action_button = QPushButton("Bond")
        self.draw_action_button = QPushButton("Draw")

        self.editor_layout.addWidget(self.carbon_button, 0, 0)
        self.editor_layout.addWidget(self.hydrogen_button, 0, 1)
        self.editor_layout.addWidget(self.bond_action_button, 0, 9)
        self.editor_layout.addWidget(self.draw_action_button, 0, 10)

        self.carbon_button.clicked.connect(self.choose_carbon)
        self.hydrogen_button.clicked.connect(self.choose_hydrogen)
        self.bond_action_button.clicked.connect(self.choose_bond_action)
        self.draw_action_button.clicked.connect(self.choose_draw_action)

        self.c = Canvas()
        self.editor_layout.addWidget(self.c, 1, 0, 20, 20)

        self.chem_logic = chem_editor_logic

    def choose_carbon(self):
        self.c.set_element(self.chem_logic.Carbon)

    def choose_hydrogen(self):
        self.c.set_element(self.chem_logic.Hydrogen)

    def choose_draw_action(self):
        self.c.set_action_type("draw")

    def choose_bond_action(self):
        self.c.set_action_type("bond")


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        # Set the background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 200, 200))  # Set the desired background color
        self.setPalette(palette)

        self.chem_logic = chem_editor_logic

        # Set default element to carbon
        self.element = self.chem_logic.Carbon

        self.atoms = []

        self.temp_bond_list = []

        self.action_type = "draw"

    def set_element(self, new_element):
        self.element = new_element

    def set_action_type(self, action):
        self.action_type = action

    def paintEvent(self, event):
        for atom in self.atoms:
            self.draw_atom_circle_from_atom(atom)
            self.draw_atom(atom)
            for bond in atom.bonds:
                self.draw_bonds(bond)
                self.draw_atom_circle(bond)
                self.draw_atoms(bond)
                self.draw_center_atom(bond)

    def draw_bonds(self, bond):
        painter = QPainter(self)
        pen = QPen()
        painter.setPen(pen)

        # Draw the bond line from one atom to another
        pen.setColor(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(QPoint(bond.atoms[0].x_coords, bond.atoms[0].y_coords),
                         QPoint(bond.atoms[1].x_coords, bond.atoms[1].y_coords))

    def draw_atom_circle(self, bond):
        painter = QPainter(self)

        # Set the brush color to match the background color
        background_color = self.palette().color(self.backgroundRole())
        brush = QBrush(background_color)
        painter.setBrush(brush)
        pen = QPen()
        pen.setStyle(Qt.PenStyle.NoPen)  # Set the pen style to NoPen
        painter.setPen(pen)

        # Draw a filled circle
        circle_center = QPointF(bond.atoms[1].x_coords, bond.atoms[1].y_coords)
        circle_radius = 12  # Adjust the radius as needed
        painter.drawEllipse(circle_center, circle_radius, circle_radius)

        circle_center = QPointF(bond.atoms[0].x_coords, bond.atoms[0].y_coords)
        painter.drawEllipse(circle_center, circle_radius, circle_radius)

    def draw_atom_circle_from_atom(self, atom):
        painter = QPainter(self)

        # Set the brush color to match the background color
        background_color = self.palette().color(self.backgroundRole())
        brush = QBrush(background_color)
        painter.setBrush(brush)
        pen = QPen()
        pen.setStyle(Qt.PenStyle.NoPen)  # Set the pen style to NoPen
        painter.setPen(pen)

        # Draw a filled circle
        circle_center = QPointF(atom.x_coords, atom.y_coords)
        circle_radius = 12  # Adjust the radius as needed
        painter.drawEllipse(circle_center, circle_radius, circle_radius)

        circle_center = QPointF(atom.x_coords, atom.y_coords)
        painter.drawEllipse(circle_center, circle_radius, circle_radius)

    def draw_atoms(self, bond):
        painter = QPainter(self)
        font = QFont("Arial", 16)  # Set the font and size
        painter.setFont(font)
        pen = QPen()
        painter.setPen(pen)
        pen.setColor(QColor(0, 0, 0))

        # Draw the letter
        letter_width = painter.fontMetrics().horizontalAdvance(bond.atoms[1].symbol)
        letter_height = painter.fontMetrics().height()
        letter_x = bond.atoms[1].x_coords - letter_width / 2
        letter_y = bond.atoms[1].y_coords + letter_height / 4
        painter.drawText(int(letter_x), int(letter_y), bond.atoms[1].symbol)

    def draw_atom(self, atom):
        painter = QPainter(self)
        font = QFont("Arial", 16)  # Set the font and size
        painter.setFont(font)
        pen = QPen()
        painter.setPen(pen)
        pen.setColor(QColor(0, 0, 0))

        # Draw the letter
        letter_width = painter.fontMetrics().horizontalAdvance(atom.symbol)
        letter_height = painter.fontMetrics().height()
        letter_x = atom.x_coords - letter_width / 2
        letter_y = atom.y_coords + letter_height / 4
        painter.drawText(int(letter_x), int(letter_y), atom.symbol)

    def draw_center_atom(self, bond):
        painter = QPainter(self)
        font = QFont("Arial", 16)  # Set the font and size
        painter.setFont(font)
        pen = QPen()
        painter.setPen(pen)
        pen.setColor(QColor(0, 0, 0))

        letter_width = painter.fontMetrics().horizontalAdvance(bond.atoms[0].symbol)
        letter_height = painter.fontMetrics().height()

        letter_x = bond.atoms[0].x_coords - letter_width / 2
        letter_y = bond.atoms[0].y_coords + letter_height / 4
        painter.drawText(int(letter_x), int(letter_y), bond.atoms[0].symbol)

    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            click_position = event.pos()
            symbol = self.element.SYMBOL

            if self.action_type == "bond":
                for atom in self.atoms:
                    atom_x = atom.x_coords
                    atom_y = atom.y_coords
                    atom_radius = 12  # Adjust the radius as needed

                    if (
                            atom_x - atom_radius <= click_position.x() <= atom_x + atom_radius and
                            atom_y - atom_radius <= click_position.y() <= atom_y + atom_radius
                    ):
                        print(f"Clicked on atom for bond: {atom.symbol}")
                        # Check if the atom has the maximum allowed bonds
                        if len(atom.bonds) < atom.outer_electrons:
                            print("Can form bond with atom", atom.symbol)
                            self.temp_bond_list.append(atom)
                            if len(self.temp_bond_list) == 2:
                                # Check if either atom already has the maximum allowed bonds
                                if len(self.temp_bond_list[0].bonds) < self.temp_bond_list[0].outer_electrons and \
                                        len(self.temp_bond_list[1].bonds) < self.temp_bond_list[1].outer_electrons:
                                    print("Can form bond between", self.temp_bond_list[0].symbol, "and",
                                          self.temp_bond_list[1].symbol)
                                    if self.temp_bond_list[0] is self.temp_bond_list[1]:
                                        print("Trying to bond to itself")
                                        self.temp_bond_list.clear()
                                        return
                                    self.temp_bond_list[0].bond(self.temp_bond_list[1])
                                    self.temp_bond_list.clear()
                                    self.update()
                                else:
                                    print("Bonding unavailable, one or both atoms have the maximum number of bonds.")
                            return
                        else:
                            print("Bonding unavailable, atom has the maximum number of bonds.")
                            print(atom.bonds)
                            return
            else:
                # Check if the letter is already in the list
                for atom in self.atoms:
                    atom_x = atom.x_coords
                    atom_y = atom.y_coords
                    atom_radius = 12  # Adjust the radius as needed

                    if (
                            atom_x - atom_radius <= click_position.x() <= atom_x + atom_radius and
                            atom_y - atom_radius <= click_position.y() <= atom_y + atom_radius
                    ):
                        print(f"Clicked on atom: {atom.symbol}")
                        return

                print(self.action_type)

                new_atom = chem_editor_logic.Atom(self.element, [click_position.x(), click_position.y()])
                self.atoms.append(new_atom)
                self.update()
