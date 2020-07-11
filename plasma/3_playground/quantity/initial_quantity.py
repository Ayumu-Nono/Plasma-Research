import numpy as np


class NumericalQuantity:
    pass


class PhysicalQuantity:
    def __init__(self):
        self.xenon_mass = 131 / 6.022E23
        self.elementary_charge = 1.602E-19

    def test(self):
        print(self.elementary_charge)
        print(self.xenon_mass)

def main():
    p = PhysicalQuantity()
    p.test()

    
if __name__ == "__main__":
    main()