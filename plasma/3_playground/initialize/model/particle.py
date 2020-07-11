import numpy as np

from ...quantity.initial_quantity import PhysicalQuantity

class ParticleModel:
    def __init__(
        self,
        pk: int,
        init_position: np.array,
        init_velocity: np.array,
    ) -> None:
        self.physical_quantity = PhysicalQuantity()
        self.position = init_position
        self.velocity = init_velocity

    def as_neutral(self) -> None:
        self.type: str = "neutral"
        self.charge: float = 0
        self.mass: float = self.physical_quantity.xenon_mass

    def as_ion(self) -> None:
        self.type:str = "ion"
        self.charge: float = self.physical_quantity.elementary_charge
        self.mass: float = self.physical_quantity.xenon_mass

    def change_status(
        self,
        new_position: np.array,
        new_velocity: np.array
    ) -> None:
        self.position = new_position
        self.velocity = new_velocity
