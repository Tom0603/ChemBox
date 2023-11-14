from PyQt6.QtCore import Qt, QPointF
from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt6.QtGui import QPainter, QPen, QColor, QFont, QFontMetrics, QPalette, QBrush

import chem_editor_logic


class ChemEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.editor_layout = QGridLayout()
        self.setLayout(self.editor_layout)

        self.carbon_button = QPushButton("C")
        self.hydrogen_button = QPushButton("H")
        self.editor_layout.addWidget(self.carbon_button, 0, 0)
        self.editor_layout.addWidget(self.hydrogen_button, 0, 1)

        self.carbon_button.clicked.connect(self.choose_carbon)
        self.hydrogen_button.clicked.connect(self.choose_hydrogen)

        self.c = Canvas()
        self.editor_layout.addWidget(self.c, 1, 0, 20, 20)

    def choose_carbon(self):
        self.c.set_letter("C")

    def choose_hydrogen(self):
        self.c.set_letter("H")


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        # Set the background color
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(200, 200, 200))  # Set the desired background color
        self.setPalette(palette)

        self.chem_logic = chem_editor_logic
        self.a = self.chem_logic.Atom("C", 4, [100, 100])
        self.b = self.chem_logic.Atom("H", 1, [100, 50], 2)
        self.c = self.chem_logic.Atom("H", 1, [50, 100], 2)
        self.d = self.chem_logic.Atom("H", 1, [100, 150], 2)
        self.e = self.chem_logic.Atom("H", 1, [150, 100], 2)
        self.a.bond(self.b)
        self.a.bond(self.c)
        self.a.bond(self.d)
        self.a.bond(self.e)

        self.letter = "C"
        self.atoms = []
        self.on_canvas = []

    def set_letter(self, new_letter):
        self.letter = new_letter

    def paintEvent(self, event):
        for bond in self.a.bonds:
            self.draw_bonds(bond)
            self.draw_atom_circle(bond)
            self.draw_atoms(bond)
            self.draw_center_atom(bond)

        for atom in self.atoms:
            self.draw_atom_circle_from_atom(atom)
            self.draw_atom(atom)

    def draw_bonds(self, bond):
        painter = QPainter(self)
        pen = QPen()
        painter.setPen(pen)

        # Draw the bond line from one atom to another
        pen.setColor(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)
        painter.drawLine(QPoint(self.a.x_coords, self.a.y_coords),
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
            symbol = self.letter

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

            new_atom = chem_editor_logic.Atom(symbol, 4, [click_position.x(), click_position.y()])
            self.atoms.append(new_atom)
            self.update()
