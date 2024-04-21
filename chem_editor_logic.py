from PyQt6.QtWidgets import QMessageBox


def show_dialog(message):
    dlg = QMessageBox()
    dlg.setWindowTitle("Invalid Action!")
    dlg.setText(f"Invalid user action!\n {message}")
    dlg.setIcon(QMessageBox.Icon.Critical)
    button = dlg.exec()

    if button == QMessageBox.StandardButton.Ok:
        print("OK!")


class Atom:
    def __init__(self, element_data: dict, coordinates: list[int, int]):
        self.symbol: str = element_data["symbol"]
        self.outer_electrons: int = element_data["outer_electrons"]
        self.x_coords: int = coordinates[0]
        self.y_coords: int = coordinates[1]
        self.full_shell: int = element_data["full_shell"]
        self.bonds: list[Bond] = []
        self.extra_electrons: int = 0
        self.overall_electrons: int = (self.outer_electrons + self.extra_electrons)

    def __eq__(self, other) -> bool:
        return self.symbol == other.symbol and [self.x_coords, self.y_coords] == [other.x_coords, other.y_coords]

    def __add_outer_electrons(self, num: int) -> None:
        self.outer_electrons += num

    def __remove_outer_electrons(self, num: int) -> None:
        self.outer_electrons -= num

    def check_is_bond_possible(self, bonding_atom, order: int = 1) -> bool:
        if (self.overall_electrons + order) > self.full_shell:
            print("Bonding unavailable, shell is full.")
            return False
        elif (bonding_atom.overall_electrons + order) > bonding_atom.full_shell:
            print("Bonding unavailable, bonding atoms shell is full.")
            return False
        else:
            return True

    def bond(self, bonding_atom, order: int = 1) -> None:
        if not self.check_is_bond_possible(bonding_atom, order):
            show_dialog("Bonding unavailable, shell is full.")
            return
        new_bond = Bond(self, bonding_atom, order)
        self.bonds.append(new_bond)
        bonding_atom.bonds.append(new_bond)

        self.extra_electrons += order
        bonding_atom.extra_electrons += order
        self.overall_electrons = (self.outer_electrons + self.extra_electrons)
        bonding_atom.overall_electrons = (bonding_atom.outer_electrons + bonding_atom.extra_electrons)

    def break_bond(self, atom, order: int = 1) -> None:
        atom.bonds = [bond for bond in atom.bonds if not (self in bond.atoms)]
        atom.__remove_outer_electrons(order)


class Bond:
    def __init__(self, atom1: Atom, atom2: Atom, order: int):
        self.atoms: list = [atom1, atom2]
        self.order: int = order

# dataclass
# lass Carbon:
#    SYMBOL: str = "C"
#    OUTER_ELECTRONS: int = 4
#    FULL_SHELL: int = 8


# dataclass
# lass Hydrogen:
#    SYMBOL: str = "H"
#    OUTER_ELECTRONS: int = 1
#    FULL_SHELL: int = 2


# dataclass
# lass Oxygen:
#    SYMBOL: str = "O"
#    OUTER_ELECTRONS: int = 6
#    FULL_SHELL: int = 8


# dataclass
# lass Chlorine:
#    SYMBOL: str = "Cl"
#    OUTER_ELECTRONS: int = 7
#    FULL_SHELL: int = 8


# dataclass
# lass Fluorine:
#    SYMBOL: str = "F"
#    OUTER_ELECTRONS: int = 7
#    FULL_SHELL: int = 8
