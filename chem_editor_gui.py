from PyQt6.QtCore import QPoint
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt6.QtGui import QPainter, QPen, QColor

import chem_editor_logic


class ChemEditor(QWidget):
    def __init__(self):
        super().__init__()

        self.editor_layout = QGridLayout()
        self.testLabel = QLabel("TestLabel")
        self.editor_layout.addWidget(self.testLabel)
        self.setLayout(self.editor_layout)  # You need to set a layout for your widget

        self.c = Canvas()
        self.editor_layout.addWidget(self.c, 2, 2, 20, 20)


class Canvas(QWidget):
    def __init__(self):
        super().__init__()

        self.chem_logic = chem_editor_logic
        self.a = self.chem_logic.Atom("C", 4, [20, 20])
        self.b = self.chem_logic.Atom("H", 1, [20, 80], 2)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen()
        pen.setColor(QColor(0, 0, 0))
        pen.setWidth(2)
        painter.setPen(pen)

        painter.drawText(self.a.x_coords, self.a.y_coords, self.a.symbol)
        painter.drawText(self.b.x_coords, self.b.y_coords, self.b.symbol)
        painter.drawLine(QPoint(self.a.x_coords + 5, self.a.y_coords + 5), QPoint(self.b.x_coords + 5, self.b.y_coords - 10))

