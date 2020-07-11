import numpy as np
import math

from pic_module import PICModule

class ElectricFieldModel(PICModule):

    """"電場を定義"""
    
    def __init__(
        self,
    ):
        pass

    def set_electric_potential(
        self,
        cell_num: int 
    ) -> None:
        potential = np.random.rand(cell_num ** 3).reshape(cell_num, cell_num, cell_num) * 10
        self.electric_potential = potential

    def calc_electric_field_on_grid(
        self,
        position: np.array
    ) -> np.array:
        x = int(position[0])
        y = int(position[1])
        z = int(position[2])
        potential = self.electric_potential
        field_x = potential[x + 1][y][z] - potential[x][y][z] 
        field_y = potential[x][y + 1][z] - potential[x][y][z]
        field_z = potential[x][y][z + 1] - potential[x][y][z]
        # WARNING: Never forget to append "-"
        return - np.array([field_x, field_y, field_z])

    def calc_electric_field_on_free_point(
        self,
        position: np.array
    ) -> np.array:
        volume_ratio_array = self.calc_volume_ratio_array(position)
        surrounding_grid_array = self.calc_surrounding_grid(position)
        electric_field = 0
        for grid_num in range(8):
            electric_field += self.calc_electric_field_on_grid(surrounding_grid_array[grid_num]) \
                * volume_ratio_array[- (grid_num + 1)]  # volumeをかける時、その組み合わせに注意
        return electric_field


    
def main():
    field = ElectricFieldModel()
    field.set_electric_potential(10)
    field.calc_electric_field_on_free_point(np.array([3.2, 4.5, 5.1]))


if __name__ == "__main__":
    main()