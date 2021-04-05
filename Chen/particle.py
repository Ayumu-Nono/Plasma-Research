import numpy as np
from numpy.lib.twodim_base import mask_indices


class Particle:
    def __init__(
        self,
        mass: float,
        charge: float,
        initial_v: np.array,
        initial_p: np.array
    ) -> None:
        self.mass: float = mass
        self.charge: float = charge
        self.velocity: np.array = initial_v
        self.position: np.array = initial_p

    def righthand_function(
        self,
        velocity: np.array,
        efield: np.array,
        mfield: np.array
    ) -> np.array:
        v = velocity
        return self.charge * (np.cross(v, mfield)  + efield) / self.mass

    def calc_position(self, timestep: float) -> np.array:
        x = self.position
        v = self.velocity
        x = x + v * timestep
        return x

    def calc_new_v(self, efield: np.array, mfield: np.array, timestep: float) -> np.array:
        v = self.velocity
        h = timestep
        k1 = self.righthand_function(v, efield=efield, mfield=mfield)
        k2 = self.righthand_function(v + (h / 2) * k1, efield=efield, mfield=mfield)
        k3 = self.righthand_function(v + (h / 2) * k2, efield=efield, mfield=mfield)
        k4 = self.righthand_function(v + h * k3, efield=efield, mfield=mfield)
        new_v = v + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        return new_v

    def update(self, efield: np.array, mfield: np.array, timestep: float) -> None:
        self.position = self.calc_position(timestep=timestep)
        self.velocity = self.calc_new_v(efield=efield, mfield=mfield, timestep=timestep)
