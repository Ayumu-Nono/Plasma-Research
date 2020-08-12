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
from utils.random_module import RandomModule


class Iterate:
    def __init__(
        self,
        init_object,
    ):
        self.init = init_object
        self.motion = CalcMotion()
        self.potential_model = ElectricPotential()
        self.calc_density = Density()
        self.random_module = RandomModule()

        for particle in self.init.neutral_list:
            density_array = self.calc_density.calc_density_array(
                position=particle.position
            )
            for grid_num in range(8):
                grid = density_array[grid_num][0]
                volume = density_array[grid_num][1]
                grid_x = grid[0]
                grid_y = grid[1]
                grid_z = grid[2]
                self.init.area.lattices_for_neutral.density[grid_x, grid_y, grid_z] += volume
        print('Start iterations ... ')

    def update_particle_model(self, particle: Particle) -> None:
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

    def push_particle_info_to_grid(self, particle: Particle):
        density_array = self.calc_density.calc_density_array(
            position=particle.position
        )
        for grid_num in range(8):
            grid = density_array[grid_num][0]
            volume = density_array[grid_num][1]
            grid_x = grid[0]
            grid_y = grid[1]
            grid_z = grid[2]
            self.init.area.lattices_for_neutral.density[grid_x, grid_y, grid_z] += volume
        
    def update_particles_model(self, particles_list: list) -> None:
        for particle in particles_list:
            self.update_particle_model(particle=particle)

    def push_particles_info_to_grid(self, particles_list: list) -> None:
        for particle in particles_list:
            self.push_particle_info_to_grid(particle=particle)

    def generate_CEX_ions(self) -> None:
        self.CEX = ChargeExchange(
            density_grid_of_neutral=self.init.area.lattices_for_neutral.density,
            density_grid_of_ion=self.init.area.lattices_for_ion.density,
            velocity_x_of_ion=self.init.area.lattices_for_ion.velocity_x,
            velocity_y_of_ion=self.init.area.lattices_for_ion.velocity_y,
            velocity_z_of_ion=self.init.area.lattices_for_ion.velocity_z,
        )
        generate_rate_array = self.CEX.generate_rate_on_grid()
        self.CEX_list: list = []
        for position_taple, generate_rate in np.ndenumerate(generate_rate_array):
            position = np.array(position_taple)
            generate_num = self.random_module.round_with_bias(generate_rate)
            for i in range(generate_num):
                particle = self.generate_CEX_ion(
                    pk=len(self.CEX_list) + 1,
                    position=position
                )
                self.CEX_list.append(particle)
                print(self.CEX_list)
        
    def generate_CEX_ion(
        self,
        pk: int,
        position: np.array,
    ) -> Particle:
        init_position = position
        init_velocity = np.random.rand(3) * 10
        particle = Particle(
            pk=pk,
            init_position=init_position,
            init_velocity=init_velocity
        )
        particle.as_ion().change_to_CEX_ion()
        return particle

    def choose_particles_in_calc_area(self) -> None:
        # 計算領域内にいる粒子だけ残す
        # neutral
        particle_list = []
        for index, particle in enumerate(self.init.neutral_list):
            if self.init.area.is_in_calc_area(position=particle.position):
                particle_list.append(particle)
        self.init.neutral_list = particle_list
        # ion
        particle_list = []
        for index, particle in enumerate(self.init.ion_list):
            if self.init.area.is_in_calc_area(position=particle.position):
                particle_list.append(particle)
        self.init.ion_list = particle_list
        
    def each_step(self) -> None:
        # print('Updating field ...')
        self.E_field_model = ElectricField(potential=self.init.area.lattices_for_neutral.density)
        self.choose_particles_in_calc_area()
        self.update_particles_model(particles_list=self.init.ion_list)
        self.update_particles_model(particles_list=self.init.neutral_list)
        self.choose_particles_in_calc_area()
        self.push_particles_info_to_grid(particles_list=self.init.ion_list)
        self.push_particles_info_to_grid(particles_list=self.init.neutral_list)
        self.generate_CEX_ions()
        
    def iterate(self):
        for timestep in tqdm(range(nq.END_STEP)):
            self.each_step()


def main():
    i = Iterate()
    print(i.init)


if __name__ == "__main__":
    main()