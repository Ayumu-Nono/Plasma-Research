import matplotlib.pyplot as plt
import numpy as np

potential = np.loadtxt('../data/potential/test.csv')

print(potential)

plt.plot(potential, label="test")
plt.show()