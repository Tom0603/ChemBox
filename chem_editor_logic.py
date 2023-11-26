from dataclasses import dataclass

from math import sqrt


@dataclass
class Atom:
    def __init__(self, element, coordinates):
        self.symbol: str = element.SYMBOL
        self.outer_electrons: int = element.OUTER_ELECTRONS
        self.x_coords: int = coordinates[0]
        self.y_coords: int = coordinates[1]
        self.full_shell: int = element.FULL_SHELL
        self.bonds = []
        self.extra_electrons: int = 0
        self.overall_electrons: int = (self.outer_electrons + self.extra_electrons)

    def bond(self, bonding_atom, order=1):
        print(self.overall_electrons)
        print(bonding_atom.overall_electrons)
        print(self.overall_electrons + order)
        print(bonding_atom.overall_electrons + order)
        if (self.overall_electrons + order) > self.full_shell:
            print("Bonding unavailable, shell is full.")
            return
        elif (bonding_atom.overall_electrons + order) > bonding_atom.full_shell:
            print("Bonding unavailable, bonding atoms shell is full.")
            return
        new_bond = Bond(self, bonding_atom, order)
        self.bonds.append(new_bond)
        bonding_atom.bonds.append(new_bond)
        self.extra_electrons += order
        bonding_atom.extra_electrons += order
        self.overall_electrons = (self.outer_electrons + self.extra_electrons)


@dataclass
class Bond:
    def __init__(self, atom1, atom2, order):
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
