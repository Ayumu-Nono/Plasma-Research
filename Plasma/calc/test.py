# グラフ書くのってどうやってやるんだっけ
import numpy as np
import matplotlib.pyplot as plt
 
x = y = np.arange(-10, 11)
u = 3
v = 3
 
x, y = np.meshgrid(x, y)
u, v = np.meshgrid(u, v)
fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))

lim = 12
for ax in axes:
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
 
    ax.set_xticks(np.arange(-lim, lim, 1))
    ax.set_yticks(np.arange(-lim, lim, 1))
 
    ax.grid()
    ax.set_aspect('equal')
 
C = np.sqrt(u * u + v * v)
axes[0].quiver(x, y, u, v)
axes[1].quiver(x, y, u, v, C, scale=100, cmap='Blues')
 
plt.show()
    