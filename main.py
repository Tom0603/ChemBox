import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from chem_editor_gui import ChemEditor

from chem_calculator import ChemCalculator

from chem_balancer import ChemBalancer
from gui_comps import TabBar


class ChemBox(QMainWindow):
    def __init__(self):
        super().__init__()

        # set window properties
        self.__left = 300
        self.__top = 300
        self.__width = 1280
        self.__height = 720
        self.__title = "ChemBox"
        self.setWindowTitle(self.__title)
        self.setGeometry(self.__left, self.__top, self.__width, self.__height)
        self.setFixedSize(self.__width, self.__height)

        self.tab_bar = TabBar()
        self.setCentralWidget(self.tab_bar)

        self.chem_calculator = ChemCalculator()

        self.tab_bar.tab1.setLayout(self.chem_calculator.main_layout)

        self.chem_balancer = ChemBalancer()
        self.tab_bar.tab2.setLayout(self.chem_balancer.balancer_layout)

        self.chem_editor = ChemEditor()
        self.tab_bar.tab3.setLayout(self.chem_editor.editor_layout)


def main():
    app = QApplication(sys.argv)

    # Load CSS file
    app.setStyleSheet(open('style.css').read())

    main_win = ChemBox()
    main_win.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
