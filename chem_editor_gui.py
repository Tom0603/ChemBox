from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen, QColor, QFont, QPalette, QBrush

import chem_editor_logic

import math


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

    def choose_carbon(self) -> None:
        self.c.set_element(self.chem_logic.Carbon)

    def choose_hydrogen(self) -> None:
        self.c.set_element(self.chem_logic.Hydrogen)

    def choose_draw_action(self) -> None:
        self.c.set_action_type("draw")

    def choose_bond_action(self) -> None:
        self.c.set_action_type("bond")


class Canvas(QWidget):
    # CONSTANTS
    ATOM_RADIUS = 12

    def __init__(self):
        super().__init__()

        # Set the background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 200, 200))
        self.setPalette(palette)

        self.chem_logic = chem_editor_logic

        # Set default element to carbon
        self.element = self.chem_logic.Carbon

        # List containing all atoms on the Canvas
        self.atoms = []

        self.temp_bond_list = []

        self.action_type = "draw"

        self.selected = False

        # Set default value of selected_atom to None
        self.selected_atom = None

    def set_element(self, new_element) -> None:
        self.element = new_element

    def set_action_type(self, action: str) -> None:
        self.action_type = action

    def paintEvent(self, event) -> None:
        for atom in self.atoms:
            self.draw_atom(atom.x_coords, atom.y_coords, atom.symbol)

            for bond in atom.bonds:
                self.draw_bonds(bond.atoms[0].x_coords, bond.atoms[0].y_coords, bond.atoms[1].x_coords,
                                bond.atoms[1].y_coords, True)
                self.draw_atom_circle(bond.atoms[1].x_coords, bond.atoms[1].y_coords, bond.atoms[0].x_coords,
                                      bond.atoms[0].y_coords)
                self.draw_atom(bond.atoms[1].x_coords, bond.atoms[1].y_coords, bond.atoms[1].symbol)
                self.draw_center_atom(bond.atoms[0].x_coords, bond.atoms[0].y_coords, bond.atoms[0].symbol)

        # Check for selected atom and draw potential positions
        if self.selected:
            if self.action_type == "bond":
                try:
                    for possible_atom in self.atoms:
                        print(self.atoms)
                        self.draw_bonds(self.selected_atom.x_coords, self.selected_atom.y_coords,
                                        possible_atom.x_coords, possible_atom.y_coords, False)
                        self.draw_atom_circle(possible_atom.x_coords, possible_atom.y_coords,
                                              self.selected_atom.x_coords,
                                              self.selected_atom.y_coords)

                        self.draw_center_atom(self.selected_atom.x_coords, self.selected_atom.y_coords,
                                              self.selected_atom.symbol)
                        self.draw_atom(possible_atom.x_coords, possible_atom.y_coords, possible_atom.symbol, False)
                except AttributeError:
                    return
                return
            print("selected")
            try:
                potential_positions = self.calc_potential_positions(self.selected_atom)
                for pos in potential_positions:
                    if not self.check_atom_overlap(pos[0], pos[1]):
                        self.draw_bonds(self.selected_atom.x_coords, self.selected_atom.y_coords, pos[0], pos[1], False)
                        self.draw_atom_circle(pos[0], pos[1], self.selected_atom.x_coords, self.selected_atom.y_coords)
                        self.draw_atom(pos[0], pos[1], self.element.SYMBOL, True)
                        self.draw_center_atom(self.selected_atom.x_coords, self.selected_atom.y_coords,
                                              self.selected_atom.symbol)
            except AttributeError:
                return

    # Function to draw potential positions for atoms
    @staticmethod
    def calc_potential_positions(atom: chem_editor_logic.Atom) -> list[tuple[int, int]]:
        x = atom.x_coords
        y = atom.y_coords
        distance = 40

        # Calculate coordinates for angles in steps of 45 degrees from 0 to 360
        coordinates_list = []
        for angle_degrees in range(0, 360, 45):
            angle_radians = math.radians(angle_degrees)
            new_x = x + distance * math.cos(angle_radians)
            new_y = y + distance * math.sin(angle_radians)
            coordinates_list.append((int(new_x), int(new_y)))

        return coordinates_list

    def check_atom_overlap(self, pos_x: int, pos_y: int) -> bool:
        atom_radius = Canvas.ATOM_RADIUS
        for atom in self.atoms:
            if (
                    atom.x_coords - atom_radius <= pos_x <= atom.x_coords + atom_radius and
                    atom.y_coords - atom_radius <= pos_y <= atom.y_coords + atom_radius
            ):
                return True

    def draw_bonds(self, atom1_x: int, atom1_y: int, atom2_x: int, atom2_y: int, actual_bond: bool = False) -> None:
        painter = QPainter(self)
        pen = QPen()

        # Draw the bond line from one atom to another
        pen.setColor(QColor(0, 0, 0))
        pen.setWidth(2)

        if not actual_bond:
            pen.setColor(QColor(255, 0, 0))
        painter.setPen(pen)

        painter.drawLine(QPoint(atom1_x, atom1_y), QPoint(atom2_x, atom2_y))

    def draw_atom_circle(self, atom1_x: int, atom1_y: int, atom2_x: int, atom2_y: int) -> None:
        painter = QPainter(self)

        # Set the brush color to match the background color
        background_color = self.palette().color(self.backgroundRole())
        brush = QBrush(background_color)
        painter.setBrush(brush)
        pen = QPen()
        pen.setStyle(Qt.PenStyle.NoPen)
        painter.setPen(pen)

        # Draw a filled circle
        circle_center = QPointF(atom2_x, atom2_y)
        circle_radius = Canvas.ATOM_RADIUS
        painter.drawEllipse(circle_center, circle_radius, circle_radius)

        circle_center = QPointF(atom1_x, atom1_y)
        painter.drawEllipse(circle_center, circle_radius, circle_radius)

    def draw_atom(self, atom_x: int, atom_y: int, symbol: str, potential: bool = False) -> None:
        painter = QPainter(self)
        font = QFont("Arial", 16)
        painter.setFont(font)
        pen = QPen()
        pen.setColor(QColor(0, 0, 0))

        if potential:
            pen.setColor(QColor(100, 100, 100))
        painter.setPen(pen)

        # Draw the letter
        letter_width = painter.fontMetrics().horizontalAdvance(symbol)
        letter_height = painter.fontMetrics().height()
        letter_x = atom_x - letter_width / 2
        letter_y = atom_y + letter_height / 4
        painter.drawText(int(letter_x), int(letter_y), symbol)

    def draw_center_atom(self, atom_x: int, atom_y: int, symbol: str) -> None:
        painter = QPainter(self)
        font = QFont("Arial", 16)
        painter.setFont(font)
        pen = QPen()
        painter.setPen(pen)
        pen.setColor(QColor(0, 0, 0))

        letter_width = painter.fontMetrics().horizontalAdvance(symbol)
        letter_height = painter.fontMetrics().height()

        letter_x = atom_x - letter_width / 2
        letter_y = atom_y + letter_height / 4
        painter.drawText(int(letter_x), int(letter_y), symbol)

    def check_clicked_on_atom(self, pos_x: int, pos_y: int) -> bool:
        atom_radius = Canvas.ATOM_RADIUS
        for atom in self.atoms:
            if (
                    atom.x_coords - atom_radius <= pos_x <= atom.x_coords + atom_radius and
                    atom.y_coords - atom_radius <= pos_y <= atom.y_coords + atom_radius
            ):
                self.selected = True
                self.selected_atom = atom
                self.update()
                return True

    def mousePressEvent(self, event) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            click_position = event.pos()

            if self.action_type == "bond":
                self.selected_atom = None
                for atom in self.atoms:
                    atom_x = atom.x_coords
                    atom_y = atom.y_coords
                    atom_radius = Canvas.ATOM_RADIUS

                    if (
                            atom_x - atom_radius <= click_position.x() <= atom_x + atom_radius and
                            atom_y - atom_radius <= click_position.y() <= atom_y + atom_radius
                    ):
                        self.selected = True
                        self.update()

                        # Check if the atom has the maximum allowed bonds
                        if len(atom.bonds) < atom.outer_electrons:
                            self.selected_atom = atom
                            self.temp_bond_list.append(atom)
                            if len(self.temp_bond_list) == 2:

                                # Check if either atom already has the maximum allowed bonds
                                if len(self.temp_bond_list[0].bonds) < self.temp_bond_list[0].outer_electrons and \
                                        len(self.temp_bond_list[1].bonds) < self.temp_bond_list[1].outer_electrons:
                                    if self.temp_bond_list[0] is self.temp_bond_list[1]:
                                        print("Trying to bond to itself")
                                        self.temp_bond_list.clear()
                                        return
                                    self.temp_bond_list[0].bond(self.temp_bond_list[1])
                                    self.temp_bond_list.clear()
                                    self.selected_atom = None
                                    self.update()
                                else:
                                    print("Bonding unavailable, one or both atoms have the maximum number of bonds.")
                            return
                        else:
                            print("Bonding unavailable, atom has the maximum number of bonds.")
                            print(atom.bonds)
                            return
                    self.selected = False
            else:
                if self.selected:
                    potential_radius = Canvas.ATOM_RADIUS
                    try:
                        if len(self.selected_atom.bonds) >= self.selected_atom.outer_electrons:
                            self.selected = False
                            self.update()
                            return
                    except AttributeError:
                        self.selected = False
                        return
                    potential_positions = self.calc_potential_positions(self.selected_atom)
                    for pos in potential_positions:
                        if not self.check_atom_overlap(pos[0], pos[1]):
                            if (
                                    pos[0] - potential_radius <= click_position.x() <= pos[0] + potential_radius and
                                    pos[1] - potential_radius <= click_position.y() <= pos[1] + potential_radius
                            ):
                                new_atom = chem_editor_logic.Atom(self.element, [pos[0], pos[1]])
                                self.atoms.append(new_atom)
                                new_atom.bond(self.selected_atom)
                                print("bonded")
                                print(self.selected_atom.symbol)
                    self.selected = False
                    self.update()
                    return

                # Check if there is an atom at clicked position
                if self.check_clicked_on_atom(click_position.x(), click_position.y()):
                    return

                print(self.action_type)

                new_atom = chem_editor_logic.Atom(self.element, [click_position.x(), click_position.y()])
                self.atoms.append(new_atom)
                self.update()
