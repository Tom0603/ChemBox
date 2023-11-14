from dataclasses import dataclass

from math import sqrt


@dataclass
class Atom:
    def __init__(self, symbol, outer_electrons, coordinates, full_shell=8):
        self.symbol = symbol
        self.outer_electrons = outer_electrons
        self.x_coords = coordinates[0]
        self.y_coords = coordinates[1]
        self.full_shell = full_shell
        self.bonds = []
        self.extra_electrons = 0
        self.overall_electrons = self.outer_electrons + self.extra_electrons

    def bond(self, bonding_atom, order=1):
        if (self.overall_electrons + order) > self.full_shell:
            return
        new_bond = Bond(self, bonding_atom, order)
        self.bonds.append(new_bond)
        bonding_atom.bonds.append(new_bond)
        self.extra_electrons += order
        bonding_atom.extra_electrons += order


@dataclass
class Bond:
    def __init__(self, atom1, atom2, order):
        self.atoms = [atom1, atom2]
        self.order = order
        self._length = self.get_bond_length()

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


def test1():
    a = Atom("C", 4, [20, 20])
    b = Atom("H", 1, [20, 30], 2)
    c = Atom("H", 1, [20, 10], 2)
    d = Atom("H", 1, [10, 20], 2)
    e = Atom("H", 1, [30, 20], 2)
    a.bond(b, 3)
    a.bond(c)
    # a.bond(d)
    # a.bond(e)
    print(a)
    print(b)

    print(a.bonds)
    print(a.bonds[0]._length)

    for bond in a.bonds:
        print(f"Bond Order: {bond.order}")
        for atom in bond.atoms:
            print(f"Atom Symbol: {atom.symbol}")


if __name__ == "__main__":
    test1()
