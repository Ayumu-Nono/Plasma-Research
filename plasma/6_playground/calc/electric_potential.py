import numpy as np
import math
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from utils.pic_module import PICModule
from utils.random_module import RandomModule
from models import physical_quantity as pq


class ElectricPotential:

    """電位を定義"""
    # TODO potentialの計算式どうする？
    
    def __init__(self):
        pass
        
    def calc_electric_potential_with_no_collision(
        self,
        ion_density: np.array
    ) -> np.array:
        k = pq.BOLTZMANN_CONSTANT
        T = pq.ELECTRON_TEMPATATURE
        e = pq.ELEMENTARY_CHARGE
        n0 = pq.PLASMA_DENSITY
        #  ここiondensityが0の時どうするの？
        potential = - k * T * np.log1p(ion_density / n0) / e
        return potential

def main():
    potential = ElectricPotentialModel()


if __name__ == "__main__":
    main()