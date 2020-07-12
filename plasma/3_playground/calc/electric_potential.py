import numpy as np
import math

# from ..initialize.model.initial_quantity import PhysicalQuantity

class ElectricPotentialModel:

    """電位を定義"""
    # TODO potentialの計算式どうする？
    
    def __init__(self):
        # self.physical_quantity = PhysicalQuantity()
        pass
        
    def calc_electric_potential_with_no_collision(
        self,
        ion_density: np.array
    ) -> np.array:
        # k = self.physical_quantity.Boltzmann_constant
        # T = self.physical_quantity.electron_temparature
        # e = self.physical_quantity.elementary_charge
        # n0 = self.physical_quantity
        k = 1.380649E-23
        T = 1.16E4 * 1
        e = 1.602E-19
        n0 = 1.6E16
        #  ここiondensityが0の時どうするの？
        potential = - k * T * np.log1p(ion_density / n0) / e
        return potential

def main():
    potential = ElectricPotentialModel()


if __name__ == "__main__":
    main()