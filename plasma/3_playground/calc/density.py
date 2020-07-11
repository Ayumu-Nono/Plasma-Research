import numpy as np

from pic_module import PICModule

class DensityModel(PICModule):

    """格子点における粒子密度を計算"""
    # TODO 粒子ひとつあたりに、現実世界の粒子何個分に相当させるか考える

    def calc_density_array(
        self,
        position: np.array
    ) -> np.array:
        volume_ratio_array = self.calc_volume_ratio_array(position)
        surrounding_grid_array = self.calc_surrounding_grid(position)
        grid_num = 0
        print(surrounding_grid_array)
        # density_array[grid_num] = 

def main():
    d = DensityModel()
    d.calc_density_array(np.array([1, 2.2, 3.4]))


if __name__ == "__main__":
    main()