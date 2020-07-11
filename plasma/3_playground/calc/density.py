import numpy as np

from pic_module import PICModule

class DensityModel(PICModule):

    """格子点における粒子密度を計算"""
    # TODO 粒子ひとつあたりに、現実世界の粒子何個分に相当させるか考える->変数self.particle_magnification

    def __init__(self):
        self.particle_magnification = 100

    def calc_density_array(
        self,
        position: np.array,
    ) -> np.array
        pass
        

def main():
    d = DensityModel()
    f = open('density_sample.csv', "w")
    cell_num = 100
    density_sample_array = np.random.rand(cell_num ** 3).reshape(cell_num, cell_num, cell_num) * 10
    
    d.calc_density_array(np.array([1, 2.2, 3.4]))


if __name__ == "__main__":
    main()