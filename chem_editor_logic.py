from dataclasses import dataclass

from math import sqrt


class Atom:

    def __init__(self, element, coordinates: list[int, int]):
        self.symbol: str = element.SYMBOL
        self.outer_electrons: int = element.OUTER_ELECTRONS
        self.x_coords: int = coordinates[0]
        self.y_coords: int = coordinates[1]
        self.full_shell: int = element.FULL_SHELL
        self.bonds: list[Bond] = []
        self.extra_electrons: int = 0
        self.overall_electrons: int = (self.outer_electrons + self.extra_electrons)

    def __eq__(self, other):
        return self.symbol == other.symbol and [self.x_coords, self.y_coords] == [other.x_coords, other.y_coords]

    def add_outer_electrons(self, num: int):
        self.outer_electrons += num

    def remove_outer_electrons(self, num: int):
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

    def bond(self, bonding_atom, order: int = 1):
        if not self.check_is_bond_possible(bonding_atom, order):
            return
        new_bond = Bond(self, bonding_atom, order)
        self.bonds.append(new_bond)
        bonding_atom.bonds.append(new_bond)

        self.extra_electrons += order
        bonding_atom.extra_electrons += order
        self.overall_electrons = (self.outer_electrons + self.extra_electrons)
        bonding_atom.overall_electrons = (bonding_atom.outer_electrons + bonding_atom.extra_electrons)

    def break_bond(self, atom, order: int = 1):
        atom.bonds = [bond for bond in atom.bonds if not (self in bond.atoms)]
        atom.remove_outer_electrons(order)


class Bond:
    def __init__(self, atom1, atom2, order: int):
        self.atoms = [atom1, atom2]
        self.order: int = order
        self._length: float = self.get_bond_length()

    def get_bond_length(self):
        """
        Get the bond length using pythagoras
        """

        x = self.atoms[1].x_coords - self.atoms[0].x_coords
        y = self.atoms[1].y_coords - self.atoms[0].y_coords
        try:
            length = sqrt(x ** 2 + y ** 2)
        except RecursionError:
            return
        return length


@dataclass
class Carbon:
    SYMBOL: str = "C"
    OUTER_ELECTRONS: int = 4
    FULL_SHELL: int = 8


@dataclass
class Hydrogen:
    SYMBOL: str = "H"
    OUTER_ELECTRONS: int = 1
    FULL_SHELL: int = 2


@dataclass
class Oxygen:
    SYMBOL: str = "O"
    OUTER_ELECTRONS: int = 6
    FULL_SHELL: int = 8


@dataclass
class Chlorine:
    SYMBOL: str = "Cl"
    OUTER_ELECTRONS: int = 7
    FULL_SHELL: int = 8


@dataclass
class Fluorine:
    SYMBOL: str = "F"
    OUTER_ELECTRONS: int = 7
    FULL_SHELL: int = 8
