import sys
import pathlib
root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

import numpy as np

from models import physical_quantity as pq


class Particle:

    """"粒子モデル"""

    def __init__(
        self,
        pk: int,  # primary_key
        init_position: np.array,
        init_velocity: np.array,
    ) -> None:
        self.pk = pk
        self.position = init_position
        self.velocity = init_velocity

    def as_neutral(self) -> None:
        self.type: str = "neutral"
        self.charge: float = 0
        self.mass: float = pq.XENON_MASS

    def as_ion(self) -> None:
        self.type = "ion"
        self.charge = pq.ELEMENTARY_CHARGE
        self.mass = pq.XENON_MASS

    def change_to_CEX_ion(self) -> None:
        self.type = "CEX"

    def change_status(
        self,
        new_position: np.array,
        new_velocity: np.array
    ) -> None:
        self.position = new_position
        self.velocity = new_velocity

