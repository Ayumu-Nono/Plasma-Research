# プラズマを粒子的に解く
import numpy as np
import matplotlib.pyplot as plt


class Calc:
    """
    計算するクラス
    """
    def __init__(self):
        self.q = 1  # 電荷
        self.magnetic_field = np.array([0, 0, 1])  # 磁場の大きさ
        self.initial_velocity = np.array([0, 1, 0])
        self.initial_position = np.array([0, 0, 0])
        self.delta_t = 0.001  # 刻み幅
        self.mass = 1 # mass

    def calc_position(self, v: np.array, x: np.array) -> np.array:
        x = x + v * self.delta_t
        return x

    def calc_delta_v(self, v: np.array, B:np.array) -> np.array:
        result = self.q * np.cross(v, B) / self.mass 
        return result

    def test(self):
        delta_v = self.calc_delta_v(self.initial_velocity, self.magnetic_field)
        v = self.initial_velocity + delta_v * self.delta_t
        x = self.calc_position(v, self.initial_position)
        f = open('data.dat', "w")
        for i in range(3):
            f.write(str(x[i]) + ' ')
        f.write("\n")
        f.close()
        print(x)
        for step in range(10):
            delta_v = self.calc_delta_v(v, self.magnetic_field)
            v = v + delta_v * self.delta_t
            x = self.calc_position(v, x)
            f = open('data.dat', "a")
            for i in range(3):
                f.write(str(x[i]) + ' ')
            f.write("\n")
            f.close()    
            print(x)

        
    def draw(self, x: np.array, y: np.array) -> None:
        plt.plot(x, y, label="test")
        plt.show()

def main():
    calc = Calc()
    calc.test()

if __name__ == '__main__':
    main()


    