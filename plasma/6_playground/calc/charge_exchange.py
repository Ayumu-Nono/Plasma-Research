import numpy as np
import math
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from utils.random_module import RandomModule
from models import numerical_quantity as nq
from models import physical_quantity as pq
from models import Particle


class ChargeExchange:
    def __init__(self):
        self.random_module = RandomModule()
    
    def is_collide(
        self,
        ion_particle: Particle,
        neutral_particle: Particle,
    ) -> bool:
        distance = np.linalg.norm(
            ion_particle.position - neutral_particle.position
        )
        collision_distance = self.numerical_quantity.collision_distance
        return distance < collision_distance

    def exchange_velocity(
        self,
        ion_particle: Particle,
        neutral_particle: Particle,
    ) -> None:
        ion_velocity = ion_particle.velocity
        neutral_velocity = neutral_particle.velocity
        ion_particle.velocity = neutral_velocity
        neutral_particle.velocity = ion_velocity

    def generate_rate(
        self,
        density_of_neutral: float,
        density_of_ion: float,
        velocity_of_neutral: np.array,
        velocity_of_ion: np.array
    ) -> float:
        n_n = density_of_neutral
        n_i = density_of_ion
        v_r = np.linalg.norm(velocity_of_ion - velocity_of_neutral)
        v_i = np.linalg.norm(velocity_of_ion)
        kinetic_energy = (1/ 2) * pq.XENON_MASS * v_i **2
        cross_section = 87.3 - 13.6 * math.log(kinetic_energy)
        generate_rate = n_n * n_i * v_r * cross_section
        return generate_rate

    def test(self):
        pass


if __name__ == "__main__":
    cex = ChargeExchangeModel()
    cex.test()