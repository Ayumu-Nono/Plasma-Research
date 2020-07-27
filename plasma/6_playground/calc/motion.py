# プラズマを粒子的に解く
import numpy as np
import matplotlib.pyplot as plt
import pathlib

current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )
from calc.electric_field import ElectricField
from utils.pic_module import PICModule
from models import physical_quantity as pq
from models import numerical_quantity as nq
from models import Particle


class CalcMotion:
    
    """動きを計算"""
    
    def __init__(self):
        # self.electric_field_model = ElectricFieldModel()
        # self.initial_velocity = np.array([1, 0, 0])
        # self.initial_position = np.array([0, 0, 0])
        # self.magnetic_field = np.array([0, 1, 0])  # 磁場の大きさ
        self.delta_t = nq.STEP_SIZE # 刻み幅
        self.q = pq.ELEMENTARY_CHARGE  # 電荷
        self.mass = pq.XENON_MASS # mass

    def righthand_function(
        self, 
        velocity: np.array,
        magnetic_field: np.array,
        electric_field: np.array
        ) -> np.array:
        v = velocity
        B = magnetic_field
        E = electric_field
        return self.q * (np.cross(v, B)  + E)/ self.mass

    def calc_new_v(self, velocity: np.array, magnetic_field: np.array, electric_field: np.array) -> np.array:
        v = velocity
        B = magnetic_field
        E = electric_field
        h = self.delta_t
        k1 = self.righthand_function(v, B, E)
        k2 = self.righthand_function(v + (h / 2) * k1, B, E)
        k3 = self.righthand_function(v + (h / 2) * k2, B, E)
        k4 = self.righthand_function(v + h * k3, B, E)
        new_v = v + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        return new_v

    def calc_new_position(
        self,
        particle: Particle,
        magnetic_field: np.array,
        electric_field: np.array
    ) -> np.array:
        new_v = self.calc_new_v(
            velocity=particle.velocity,
            magnetic_field=magnetic_field,
            electric_field=electric_field
        )
        old_x = particle.position
        new_x = old_x + new_v * self.delta_t
        # particleモデルの更新
        particle.position = new_x
        particle.position = new_v
        return new_x

    def test(self):
        self.electric_field_model.set_electric_potential(100)
        electric_field = self.electric_field_model.calc_electric_field_on_free_point(self.initial_position)
        new_v = self.calc_new_v(self.initial_velocity, self.magnetic_field, electric_field)
        new_x = self.calc_position(new_v, self.initial_position)
        time = self.delta_t
        f = open('data.csv', "w")
        f.write('time,position_x,position_y,position_z,velocity_x,velocity_y,velocity_z,\n')
        f.write(str(time) + ',')
        for i in range(3):
            f.write(str(new_x[i]) + ',')
        for i in range(3):
            f.write(str(new_v[i]) + ',')
        f.write("\n")
        f.close()
        # print(new_x)
        for step in range(5000):
            time = time + self.delta_t
            v = new_v
            x = new_x
            electric_field = self.electric_field_model.calc_electric_field_on_free_point(x)
            new_v = self.calc_new_v(v, self.magnetic_field, electric_field)
            new_x = self.calc_position(v, x)
            f = open('data.csv', "a")
            f.write(str(time) + ',')
            for i in range(3):
                f.write(str(new_x[i]) + ',')
            for i in range(3):
                f.write(str(new_v[i]) + ',')
            f.write("\n")
            f.close()    
            # print(new_x)

        
    def draw(self, x: np.array, y: np.array) -> None:
        plt.plot(x, y, label="test")
        plt.show()

def main():
    calc = Calc()
    calc.test()

if __name__ == '__main__':
    main()
