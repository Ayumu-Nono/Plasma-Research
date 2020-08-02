import sys
import pathlib

import numpy as np
from tqdm import tqdm

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from calc.charge_exchange import ChargeExchange
from calc.density import Density
from calc.electric_field import ElectricField
from calc.electric_potential import ElectricPotential
from calc.motion import CalcMotion
from managers.initialize import Initialize
from models import numerical_quantity as nq
from models.particle import Particle


class Iterate:
    def __init__(
        self,
        init_object,
    ):
        self.init = init_object
        self.motion = CalcMotion()
        self.potential_model = ElectricPotential()
        self.calc_density = Density()
        self.cex = ChargeExchange()
        self.lattices = self.init.area.lattices
        for particle in self.init.ion_list:
            density_array = self.calc_density.calc_density_array(
                position=particle.position
            )
            for grid_num in range(8):
                grid = density_array[grid_num][0]
                volume = density_array[grid_num][1]
                grid_x = grid[0]
                grid_y = grid[1]
                grid_z = grid[2]
                self.lattices[grid_x, grid_y, grid_z] += volume
        print('Start iterations ... ')

    def update_particles_model(self, particle: Particle) -> None:
        E_field = self.E_field_model.calc_electric_field_on_free_point(
            position=particle.position
        )
        B_field = np.array([0, 0, 0])
        # new positionを計算しつつモデルも更新
        self.motion.calc_new_position(
            particle=particle,
            magnetic_field=B_field,
            electric_field=E_field
        )
        # print('Updated. Particles number is ', len(particle_list))

    def push_info_to_grid(self, particle: Particle):
        density_array = self.calc_density.calc_density_array(
            position=particle.position
        )
        for grid_num in range(8):
            grid = density_array[grid_num][0]
            volume = density_array[grid_num][1]
            grid_x = grid[0]
            grid_y = grid[1]
            grid_z = grid[2]
            self.lattices[grid_x, grid_y, grid_z] += volume

    def calc_cex_rate(self) -> None:
        pass

    def choose_particles_in_calc_area(self) -> None:
        # 計算領域内にいる粒子だけ残す
        particle_list = []
        for index, particle in enumerate(self.init.ion_list):
            if self.init.area.is_in_calc_area(position=particle.position):
                particle_list.append(particle)
        self.init.ion_list = particle_list

    def each_step(self) -> None:
        # print('Updating field ...')
        self.E_field_model = ElectricField(potential=self.lattices)
        self.choose_particles_in_calc_area()
        for particle in self.init.ion_list:
            self.update_particles_model(particle=particle)
        # print('Pushing to grid ...')
        self.lattices = self.init.area.lattices
        self.choose_particles_in_calc_area()
        for particle in self.init.ion_list:
            self.push_info_to_grid(particle=particle)

    def iterate(self):
        for timestep in tqdm(range(nq.END_STEP)):
            self.each_step()


def main():
    i = Iterate(particles_num=10000)
    i.iterate()


if __name__ == "__main__":
    main()