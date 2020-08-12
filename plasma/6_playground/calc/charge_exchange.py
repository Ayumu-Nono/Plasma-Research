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
        density_grid_of_neutral: np.array,
        density_grid_of_ion: np.array,
        velocity_x_of_ion: np.array,
        velocity_y_of_ion: np.array,
        velocity_z_of_ion: np.array
    ) -> None:
        self.random_module = RandomModule()
        self.density_grid_of_neutral = density_grid_of_neutral
        self.density_grid_of_ion = density_grid_of_ion
        self.velocity_list_of_ion: list = [
            velocity_x_of_ion,
            velocity_y_of_ion,
            velocity_z_of_ion
        ]

    def calc_ave_velocity_on_all_grid(
        self,
        velocity_grid_in_sum: np.array,
        density_grid_of_ion: np.array
    ) -> np.array:
        velocity_grid_in_ave = np.divide(
            velocity_grid_in_sum,
            density_grid_of_ion,
            out=np.zeros_like(density_grid_of_ion),
            where=density_grid_of_ion!=0)
        return velocity_grid_in_ave

    def average_velocity_list_of_ion(self) -> None:
        new_velocity_list_of_ion = []
        for velocity_array in self.velocity_list_of_ion:
            new_velocity_array = self.calc_ave_velocity_on_all_grid(
                velocity_grid_in_sum=velocity_array,
                density_grid_of_ion=self.density_grid_of_ion
            )
            new_velocity_list_of_ion.append(new_velocity_array)
        self.averaged_velocity_list_of_ion = new_velocity_list_of_ion

    def calc_velocity_norm(self) -> np.array:
        velocity_x = self.averaged_velocity_list_of_ion[0]
        velocity_y = self.averaged_velocity_list_of_ion[1]
        velocity_z = self.averaged_velocity_list_of_ion[2]
        velocity_norm: np.array = velocity_x**2 + velocity_y**2 + velocity_z**2
        velocity_norm = np.sqrt(velocity_norm)
        return velocity_norm

    def generate_rate_on_grid(self) -> np.array:
        self.average_velocity_list_of_ion()  # まず速度を平均化する
        n_n: np.array = self.density_grid_of_neutral
        n_i: np.array = self.density_grid_of_ion
        v_r: np.array = self.calc_velocity_norm()
        v_i: np.array = self.calc_velocity_norm()
        kinetic_energy: np.array = (1 / 2) * pq.XENON_MASS * v_i ** 2
        cross_section: np.array = 87.3 - 13.6 * np.log1p(kinetic_energy)
        generate_rate: np.array = n_n * n_i * v_r * cross_section
        return generate_rate

    def test(self):
        pass


if __name__ == "__main__":
    cex = ChargeExchange()
    cex.test()