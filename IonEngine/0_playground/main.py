from typing import List

import numpy as np

from particle import Particle
from draw import Draw

p = Particle()
d = Draw()


class NewtonDynamics(object):

    data: List[float] = []

    def __init__(self, *args):
        super(NewtonDynamics, self).__init__(*args)
        self._acceration = np.array([2, 0])

    def setParticle(self):
        p.setMass(1)
        p.setInitialVerosity(np.array([0, 0]))
        p.setInitialPosition(np.array([0, 5]))

    def CalcPosition(self, time):
        t = time
        r = p._x0 + p._v0 * t + (1 / 2) * self._acceration * t ** 2

        return r

    def print_position(self):
        for i in range(0, 10 + 1):
            data_box = [0, 0, 0]
            data_box[0] = i
            data_box[1] = self.CalcPosition(i)[0]
            data_box[2] = self.CalcPosition(i)[1]

            print(data_box)

            self.data.append(data_box)
        print(self.data)

    def Output(self, path):
        f = open(path, "w")
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data[i])):
                f.write(str(self.data[i][j]) + ",")
            f.write("\n")
        f.close()


def main():
    n = NewtonDynamics()
    n.setParticle()
    n.print_position()
    n.Output("output.csv")
    d.drawGraph()


if __name__ == "__main__":
    main()
