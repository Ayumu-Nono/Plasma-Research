import numpy as np
import math
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from utils.random_module import RandomModule
from utils.pic_module import PICModule
from models import numerical_quantity as nq
from models import physical_quantity as pq
from models import Particle


class ChargeExchange(PICModule):
    
    def __init__(
        self,
        density_grid: np.array,
        velocity_x: np.array,
        velocity_y: np.array,
        velocity_z: np.array
    ) -> None:
        self.random_module = RandomModule()
        self.density_grid = density_grid
        self.velocity_list = [velocity_x, velocity_y, velocity_z]

    def calc_ave_velocity_on_all_grid(
        self,
        velocity_grid_in_sum: np.array,
        density_grid: np.array
    ) -> np.array:
        velocity_grid_in_ave = np.divide(
            velocity_grid_in_sum,
            density_grid,
            out=np.zeros_like(density_grid),
            where=density_grid!=0)
        return velocity_grid_in_ave

    def average_velocity_list(self) -> None:
        new_velocity_list = []
        for velocity_array in self.velocity_list:
            new_velocity_array = self.calc_ave_velocity_on_all_grid(
                velocity_grid_in_sum=velocity_array,
                density_grid=self.density_grid
            )
            new_velocity_list.append(new_velocity_array)
        self.velocity_list = new_velocity_list

    def generate_rate(
        self,
        density_of_neutral: float,
        density_of_ion: float,
        velocity_of_neutral: np.array,
        velocity_of_ion: np.array
    ) -> float:
        n_n = density_of_neutral
        n_i = density_of_ion
        v_r = np.linalg.norm(velocity_of_ion - velocity_of_neutral)
        v_i = np.linalg.norm(velocity_of_ion)
        kinetic_energy = (1 / 2) * pq.XENON_MASS * v_i ** 2
        cross_section = 87.3 - 13.6 * math.log(kinetic_energy)
        generate_rate = n_n * n_i * v_r * cross_section
        return generate_rate

    def test(self):
        pass


if __name__ == "__main__":
    cex = ChargeExchange()
    cex.test()