import numpy as np
import math

from .random_module import RandomModule
from ..initialize.model.initial_quantity import PhysicalQuantity()

class ChargeExchangeModel:
    def __init__(self):
        self.random_module = RandomModule()
        self.physical_quantity = PhysicalQuantity()
    
    def is_collide(
        self,
        ion_particle,
        neutral_particle,
    ) -> bool:
        distance = np.linalg.norm(
            ion_particle.position - neutral_particle
        )
        
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
        kinetic_energy = (1/ 2) * self.physical_quantity.xenon_mass * v_i **2
        cross_section = 87.3 - 13.6 * math.log(kinetic_energy)
        generate_rate = n_n * n_i * v_r * cross_section
        return generate_rate

    def test(self):
        pass


if __name__ == "__main__":
    cex = ChargeExchangeModel()
    cex.test()