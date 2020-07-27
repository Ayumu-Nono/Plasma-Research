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


class Iterate:
    def __init__(
        self,
        particles_num: int,
    ):
        self.motion = CalcMotion()
        print('initializing all in Class "Iterate" ...')
        self.potential_model = ElectricPotential()
        self.init = Initialize(particles_num)
        self.init.init_all()
        self.calc_density = Density()
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

    def update_particles_model(self):
        # print('Updating field ...')
        E_field_model = ElectricField(potential=self.lattices)
        # 計算領域内にいる粒子だけ残す
        particle_list = []
        for index, particle in enumerate(self.init.ion_list):
            if self.init.area.is_in_calc_area(position=particle.position):
                particle_list.append(particle)
        self.init.ion_list = particle_list
        # 選別メソッドここまで
        for particle in self.init.ion_list:
            E_field = E_field_model.calc_electric_field_on_free_point(
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

    def push_info_to_grid(self):
        # print('Pushing to grid ...')
        self.lattices = self.lattices = self.init.area.lattices
        # 計算領域内にいる粒子だけ残す
        particle_list = []
        for index, particle in enumerate(self.init.ion_list):
            if self.init.area.is_in_calc_area(position=particle.position):
                particle_list.append(particle)
        self.init.ion_list = particle_list
        # 選別メソッドここまで
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
        
    def iterate(self):
        for timestep in tqdm(range(nq.END_STEP)):
            self.update_particles_model()
            self.push_info_to_grid()
        

def main():
    i = Iterate(particles_num=10000)
    i.iterate()


if __name__ == "__main__":
    main()