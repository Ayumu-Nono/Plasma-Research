import numpy as np
import pandas as pd

from model.particle_model import ParticleModel


class InitializeNeutralPatricles:
    def __init__(
        self,
        particles_num: int
    ):
        self.particles_num = particles_num

    def make_particles(self) -> None:
        self.particle_list = []
        for pk in range(self.particles_num):
            init_position = np.array([1, 1, 1])
            init_velocity = np.array([2, 2, 2])
            self.particle_list.append(ParticleModel(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            ))

    def test(self):
        self.make_particles()
        print((self.particle_list))

def main():
    init = InitializeNeutralPatricles(particles_num=10)
    init.test()


if __name__ == "__main__":
    main()
