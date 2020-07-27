import numpy as np
import math
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models import Particle

class InitNeutralParticles:

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
            particle = Particle(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            )
            particle.as_neutral()
            self.particle_list.append(particle)

    def test(self):
        self.make_particles()
        print(self.particle_list)

class InitIonizedPatricles:

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
            particle = Particle(
                pk=pk,
                init_position=init_position,
                init_velocity=init_velocity
            )
            particle.as_ion()
            self.particle_list.append(particle)

if __name__ == "__main__":
    i = InitNeutralParticles(particles_num=10)
    i.test()