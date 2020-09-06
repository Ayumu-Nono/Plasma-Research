import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Show:
    def __init__(self, path):
        self.path = path
        self.df = pd.read_csv(self.path, header=0, sep=',')

    def draw(self):
        X = self.df['position_x'].values
        Y = self.df['position_y'].values
        Z = self.df['position_z'].values
        fig = plt.figure()
        ax = Axes3D(fig)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.plot(X, Y, Z, marker='o', linestyle='None')

        # plt.show()
        plt.savefig('../outdata/fig/figure.png')

    def sequence(self):
        self.draw()
        print(self.df)




if __name__ == "__main__":
    s = Show(path="../outdata/neutrals.csv")
    s.sequence()