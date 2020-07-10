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

    def change_status(
        self,
        new_position: np.array,
        new_velocity: np.array
    ) -> None:
        self.position = new_position
        self.velocity = new_velocity
