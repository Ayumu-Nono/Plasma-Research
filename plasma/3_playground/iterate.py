import numpy as np
import pandas as pd

from init_all import InitAll
from calc.density import DensityModel
from calc.electric_potential import ElectricPotentialModel
from calc.electric_field import ElectricFieldModel
from calc.motion import CalcMotion

class Iterate:
    def __init__(
        self,
        particles_num: int,
    ):
        self.motion = CalcMotion()
        print('initializing all in Class "Iterate" ...')
        self.potential_model = ElectricPotentialModel()
        self.init = InitAll(particles_num)
        self.init.make_calc_area(10, 1, 1, 2)
        self.init.make_particles()
        self.calc_density = DensityModel()
        for particle_pk in range(len(self.init.ion.particle_list)):
            density_array = self.calc_density.calc_density_array(self.init.ion.particle_list[particle_pk].position)
            for grid_num in range(8):
                grid = density_array[grid_num][0]
                volume = density_array[grid_num][1]
                grid_x = grid[0]
                grid_y = grid[1]
                grid_z = grid[2]
                self.init.area.latice[grid_x, grid_y, grid_z] += volume
        self.latice = self.init.area.latice

    def update_particles_model(self):
        print('Updating field ...')
        E_field_model = ElectricFieldModel(potential=self.latice)
        # 計算領域内にいる粒子だけ残す
        particle_list = []
        for index, particle in enumerate(self.init.ion.particle_list):
            if self.init.area.is_in_calc_area(position=particle.position):
                particle_list.append(particle)
        self.init.ion.particle_list = particle_list
        ## 選別メソッドここまで
        for particle in self.init.ion.particle_list:
            E_field = E_field_model.calc_electric_field_on_free_point(position=particle.position)
            B_field = np.array([0, 0, 0])
            # new positionを計算しつつモデルも更新
            self.motion.calc_new_position(
                particle=particle,
                magnetic_field=B_field,
                electric_field=E_field
            )
        print('Updated. Particles number is ', len(particle_list))
        
    def test(self):
        self.update_particles_model()
        pass

def main():
    i = Iterate(particles_num=100)
    i.test()


if __name__ == "__main__":
    main()