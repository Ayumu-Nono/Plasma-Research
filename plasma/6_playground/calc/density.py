import numpy as np
import math
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )
from utils.pic_module import PICModule
from utils.random_module import RandomModule


class DensityModel(PICModule):

    """格子点における粒子密度を計算"""
    # TODO 粒子ひとつあたりに、現実世界の粒子何個分に相当させるか考える->変数self.particle_magnification

    def __init__(self):
        self.particle_magnification = 100
        self.pic = PICModule()

    def calc_density_array(
        self,
        position: np.array,
    ) -> list:
        surrounding_grid_array = self.pic.calc_surrounding_grid(position)
        volume_array = self.pic.calc_volume_array(position)
        grid_volume_set_list = []
        for grid_num in range(8):
            grid_volume_set_list.append(
                [surrounding_grid_array[grid_num], volume_array[grid_num]]
            )
        grid_volume_set_array = np.array(grid_volume_set_list)
        return grid_volume_set_array

def main():
    d = DensityModel()
    # f = open('density_sample.csv', "w")
    # cell_num = 100
    # density_sample_array = np.random.rand(cell_num ** 3).reshape(cell_num, cell_num, cell_num) * 10
    
    d.calc_density_array(np.array([1, 2.2, 3.4]))


if __name__ == "__main__":
    main()