import numpy as np
import math
import pathlib
import sys


root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models import Particle, CalcArea
from models import numerical_quantity as nq


class Initialize:
    def __init__(self, particles_num: int):
        self.particles_num = particles_num

    def init_calc_area(self) -> None:
        self.area = CalcArea()

    def init_neutral_particles(self) -> None:
        self.neutral_list = []
        for pk in range(self.particles_num):
            init_position = np.random.rand(3) * 10
            init_velocity = np.random.rand(3) * 10
            particle = Particle(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            )
            particle.as_neutral()
            self.neutral_list.append(particle)

    def init_ion_particles(self) -> None:
        self.ion_list = []
        for pk in range(self.particles_num):
            init_position = np.random.rand(3) * 10
            init_velocity = np.random.rand(3) * 10
            particle = Particle(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            )
            particle.as_ion()
            self.ion_list.append(particle)

    def init_all(self) -> None:
        self.init_calc_area()
        self.init_ion_particles()
        self.init_neutral_particles()


def main():
    init = Initialize(particles_num=10)
    init.init_all()
    print(1)
    print(init.area.lattices)


if __name__ == "__main__":
    main()
