import numpy as np
import math


class RandomModule:
    def Box_Muller_method_3D(self) -> np.array:
        x = np.random.rand(4)
        r1 = math.sqrt(- 2 * math.log(1 - x[0])) * math.sin(2 * math.pi * x[1])
        r2 = math.sqrt(- 2 * math.log(1 - x[1])) * math.cos(2 * math.pi * x[0])
        r3 = math.sqrt(- 2 * math.log(1 - x[3])) * math.cos(2 * math.pi * x[2])
        r = np.array([r1, r2, r3])
        return r

    def test(self):
        f = open('test.csv', 'w')
        f.write("x,y,z\n")
        for i in range(100):
            x = self.Box_Muller_method_3D()
            f.write(str(x[0]) + ',' + str(x[1]) + ',' + str(x[2]) + '\n')





if __name__ == "__main__":
    r = RandomModule()
    r.test()