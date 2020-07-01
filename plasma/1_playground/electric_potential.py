import numpy as np
import math


class ElectricPotentialModel:
    def __init__:
        self.Boltzmann_constant = 1.380649E-23
        self.electron_temparature = 1.16E4  # 適当

    def calc_electric_potential_without_magnetic_field(
        self,
        ion_density: float
    ) -> float:
        k = self.Boltzmann_constant
        T = self.electron_temparature
        potential = k * T * math.log(ion_density)
        return potential

def main():
    potential = ElectricPotentialModel()


if __name__ == "__main__":
    main()