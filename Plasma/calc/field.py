# 場を定義する
import numpy as np
import matplotlib.pyplot as plt


class Field:
    def __init__(self):
        self.Efield = 0  # 電場

    def set_Efield(self, xlim, ylim):
        x = np.arange(xlim)
        y = np.arange(xlim)
        x, y = np.meshgrid(x, y)
        u = 1  # 電場ベクトル
        v = 0  # 電場ベクトル
        print(u)
        u, v = np.meshgrid(u, v)
        
        return [x, y, u, v]
        

def main():
    f = Field() 
    Efield = f.set_Efield(10, 10)
    x = Efield[0]
    y = Efield[1]
    u = Efield[2]
    v = Efield[3]

    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    lim = 10
    for ax in axes:
        ax.set_xlim(-1, lim)
        ax.set_ylim(-1, lim)

        ax.set_xticks(np.arange(-1, lim, 1))
        ax.set_yticks(np.arange(-1, lim, 1))

        ax.grid()
        ax.set_aspect('equal')

    C = np.sqrt(u * u + v * v)
    axes[0].quiver(x, y, u, v)
    axes[1].quiver(x, y, u, v, C, scale=100, cmap='Blues')

    plt.show()
    

if __name__ == "__main__":
    main()