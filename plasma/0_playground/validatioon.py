import numpy as np
import pandas as pd
from scipy.optimize import curve_fit


class Validation:
    def __init__(self, inputdata):
        self.data = pd.read_csv(inputdata)

    def nonlinear_fit(self, t, a, b, c, d):
        return a * np.sin(b * t + c) + d 

    def test(self):
        print(self.data)
        param, cov = curve_fit(
            self.nonlinear_fit,
            self.data['time'].values,
            self.data['position_y'].values
            )
        print(param)
        print(cov)
        return param

    def remake(self, t, param: list):
        return param[0] * np.sin(param[1] * t + param[2]) + param[3]

    def output(self, outfile):
        pass

def main():
    v = Validation('data.csv')
    v.test()


if __name__ == "__main__":
    main()