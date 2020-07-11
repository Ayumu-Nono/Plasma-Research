import numpy as np
import math

from ..quantity.initial_quantity import PhysicalQuantity

class ElectricPotentialModel:

    """電位を定義"""
    
    def __init__(self):
        self.physical_quantity = PhysicalQuantity()
        
    def calc_electric_potential_with_no_collision(
        self,
        ion_density: float
    ) -> float:
        k = self.physical_quantity.Boltzmann_constant
        T = self.physical_quantity.electron_temparature
        potential = k * T * math.log(ion_density)
        return potential

def main():
    potential = ElectricPotentialModel()


if __name__ == "__main__":
    main()