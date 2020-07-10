import numpy as np


class ParticleModel:
    # default
    self.type: str = "neutral"
    self.charge: float = 0
    self.mass: float = 131 / 6.022E23

    def __init__(
        self,
        pk: int,
        init_position: np.array,
        init_velocity: np.array,
    ) -> None:
        self.position = init_position
        self.velocity = init_velocity

    def as_neutral(self) -> None:
        pass

    def as_ion(self) -> None:
        self.type = "ion"
        self.charge = 1.602E-19

    # def as_electron(self) -> None:
    #     self.type = "electron"
    #     self.charge = 1.602E-19

    def change_status(
        self,
        new_position: np.array,
        new_velocity: np.array
    ) -> None:
        self.position = new_position
        self.velocity = new_velocity
