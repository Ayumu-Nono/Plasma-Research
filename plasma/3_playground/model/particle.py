import numpy as np


class ParticleModel:
    def __init__(
        self,
        pk: int,
        init_position: np.array,
        init_velocity: np.array,
    ) -> None:
        self.position = init_position
        self.velocity = init_velocity

    def as_neutral(self) -> None:
        self.type: str = "neutral"
        self.charge: float = 0
        self.mass: float = 131 / 6.022E23

    def as_ion(self) -> None:
        self.type:str = "ion"
        self.charge: float = 1.602E-19
        self.mass: float = 131 / 6.022E23

    def change_status(
        self,
        new_position: np.array,
        new_velocity: np.array
    ) -> None:
        self.position = new_position
        self.velocity = new_velocity
