import numpy as np
import math

from ..initialize.model.initial_quantity import PhysicalQuantity

class ElectricPotentialModel:

    """電位を定義"""
    
    def __init__(self):
        self.physical_quantity = PhysicalQuantity()
        
    def calc_electric_potential_with_no_collision(
        self,
        ion_density: np.array
    ) -> np.array:
        k = self.physical_quantity.Boltzmann_constant
        T = self.physical_quantity.electron_temparature
        e = self.physical_quantity.elementary_charge
        n0 = self.physical_quantity
        if ion_density == 0:
            return 0
        else:
            potential = - k * T * math.log(ion_density / self.physical_quantity.plasma_density) / e
            return potential

def main():
    potential = ElectricPotentialModel()


if __name__ == "__main__":
    main()