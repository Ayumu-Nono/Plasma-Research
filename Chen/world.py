from typing import List
import numpy as np



class Lattice:
    def __init__(
        self,
        efield: list,
        mfield: list
    ) -> None:
        self.efield: np.array = np.array(efield)
        self.mfield: np.array = np.array(mfield)


class World:
    def __init__(self) -> None:
        self.field = None

    def set_field(self, efield: list, mfield: list) -> None:
        self.field = Lattice(efield=efield, mfield=mfield)