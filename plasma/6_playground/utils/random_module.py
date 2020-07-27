import numpy as np
import math
import random


class RandomModule:
    def Box_Muller_method_3D(self) -> np.array:
        x = np.random.rand(4)
        r1 = math.sqrt(- 2 * math.log(1 - x[0])) * math.sin(2 * math.pi * x[1])
        r2 = math.sqrt(- 2 * math.log(1 - x[1])) * math.cos(2 * math.pi * x[0])
        r3 = math.sqrt(- 2 * math.log(1 - x[3])) * math.cos(2 * math.pi * x[2])
        r = np.array([r1, r2, r3])
        return r

    def round_with_bias(self, hoge: float):
        hoge_int = math.floor(hoge)
        hoge_float = hoge
        decimal_part = hoge_float - hoge_int
        random_num = random.random()
        if random_num > decimal_part:
            hoge = hoge_int
        else:
            hoge = hoge_int + 1
        return hoge
