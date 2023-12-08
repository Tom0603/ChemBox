import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QTableWidget, QTableWidgetItem

from chem_editor_gui import ChemEditor

from chem_calculator import MolesCalculator, ConcCalculator, AvogadroCalculator, IdealGasLawCalculator
from chem_balancer import ChemBalancer
from gui_comps import TabBar, SideBar


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

        self.moles_calc = MolesCalculator()
        self.concentration_calc = ConcCalculator()
        self.avogadro_calc = AvogadroCalculator()

        # Initialise moles tab in sidebar
        self.side_bar.moles_tab.setLayout(self.moles_calc.moles_layout)

        # Initialise concentration tab in sidebar
        self.side_bar.conc_tab.setLayout(self.concentration_calc.conc_layout)

        # Initialise avogadro's calculator tab in sidebar
        self.side_bar.avogadro_tab.setLayout(self.avogadro_calc.avogadro_layout)

        # Initialise igl tab in sidebar
        self.ideal_gas_law = IdealGasLawCalculator()
        self.side_bar.ideal_gas_tab.setLayout(self.ideal_gas_law.ideal_gas_layout)

        self.chem_balancer = ChemBalancer()
        self.tab_bar.tab3.setLayout(self.chem_balancer.balancer_layout)

        self.chem_editor = ChemEditor()
        self.tab_bar.tab5.setLayout(self.chem_editor.editor_layout)

        # self.interactiveTable = InteractiveTable()
        # self.tabBar.tab2.setLayout(self.interactiveTable.tableLayout)


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
