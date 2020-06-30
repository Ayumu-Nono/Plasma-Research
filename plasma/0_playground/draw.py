from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Draw:
    def __init__(self, datafile):
        self.data = pd.read_csv(datafile)

    def draw(self):
        X = self.data['position_x'].values
        Y = self.data['position_y'].values
        Z = self.data['position_z'].values
        fig = plt.figure()
        ax = Axes3D(fig)

        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_zlabel('Z')

        ax.plot(X, Y, Z, marker='o', linestyle='None')

        # plt.show()
        plt.savefig('figure.png')

def main():
    d = Draw('data.csv')
    d.draw()


if __name__ == "__main__":
    main()