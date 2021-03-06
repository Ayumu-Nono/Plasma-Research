import numpy as np
import pandas as pd

from .model.particle import ParticleModel

class NeutralPatricles:

    """中性粒子を初期配置"""
    # TODO 初期ポジションと初期速度をちゃんと分布で定義

    def __init__(
        self,
        particles_num: int
    ):
        self.particles_num = particles_num

    def make_particles(self) -> None:
        self.particle_list = []
        for pk in range(self.particles_num):
            init_position = np.random.rand(3) * 10
            init_velocity = np.random.rand(3) * 10
            particle = ParticleModel(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            )
            particle.as_neutral()
            self.particle_list.append(particle)


class IonizedPatricles:

    """イオン粒子を初期配置"""
    # TODO 初期ポジションと初期速度をちゃんと分布で定義

    def __init__(
        self,
        particles_num: int
    ):
        self.particles_num = particles_num

    def make_particles(self) -> None:
        self.particle_list = []
        for pk in range(self.particles_num):
            init_position = np.random.rand(3) * 9
            init_velocity = np.random.rand(3) * 9
            particle = ParticleModel(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            )
            particle.as_ion()
            self.particle_list.append(particle)


def main():
    init = InitializeNeutralPatricles(particles_num=3)
    init.test()


if __name__ == "__main__":
    main()
