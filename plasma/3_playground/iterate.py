import numpy as np
import pandas as pd

from init_all import InitAll
from calc.density import DensityModel
from calc.electric_potential import ElectricPotentialModel
from calc.electric_field import ElectricFieldModel

class Iterate:
    def __init__(
        self,
        initial_position_csv: str,
        particles_num: int,
    ):
        print('initializing all in Class "Iterate" ...')
        self.potential_model = ElectricPotentialModel()
        self.init = InitAll(particles_num)
        self.initial_position_csv = initial_position_csv
        self.init.make_calc_area(10, 1, 3, 2)
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
        print(self.potential_model.calc_electric_potential_with_no_collision(self.init.area.latice))

    def update_field(self):
        E_field_model = ElectricFieldModel(potential=self.latice)
        E_field = E_field_model.calc_electric_field_on_free_point(np.array([1,2,3]))
        print(E_field)

    # def read_initial_position(self):
    #     df = pd.read_csv(self.initial_position_csv)
    #     self.df = df[['position_x', 'position_y', 'position_z']]
    #     print(self.df.values)

    # def 

    def test(self):
        self.update_field()
        pass

def main():
    i = Iterate('result/position.csv', particles_num=1000)
    i.test()


if __name__ == "__main__":
    main()