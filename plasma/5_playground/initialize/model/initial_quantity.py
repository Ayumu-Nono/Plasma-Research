import numpy as np


class NumericalQuantity:
    
    """計算に用いる定数"""

    def __init__(self):
        self.collision_distance = 1E-3


class PhysicalQuantity:

    """物理量"""
    
    def __init__(self):
        self.xenon_mass = 131 / 6.022E23
        self.elementary_charge = 1.602E-19
        self.Boltzmann_constant = 1.380649E-23  # [J K^-1]
        self.electron_temparature = 1.16E4 * 1  # [K] 数値は適当
        self.plasma_density = 1.6E16  # [m^-3]  数値は割と適当

    def test(self):
        print(self.elementary_charge)
        print(self.xenon_mass)

def main():
    p = PhysicalQuantity()
    p.test()

    
if __name__ == "__main__":
    main()