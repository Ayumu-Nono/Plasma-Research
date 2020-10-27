import numpy as np
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models import numerical_quantity as nq


class Lattices:

    """格子モデル"""
    def __init__(self, lattice_type: str) -> None:
        self.type = lattice_type
        self.density = np.zeros((nq.LATTICE_NUM, nq.LATTICE_NUM, nq.LATTICE_NUM))
        self.velocity_x = np.zeros((nq.LATTICE_NUM, nq.LATTICE_NUM, nq.LATTICE_NUM))
        self.velocity_y = np.zeros((nq.LATTICE_NUM, nq.LATTICE_NUM, nq.LATTICE_NUM))
        self.velocity_z = np.zeros((nq.LATTICE_NUM, nq.LATTICE_NUM, nq.LATTICE_NUM))

    def is_out_of_lattices(
        self,
        position: np.array
    ) -> bool:
        is_out_of_area = (
            position[0] > 1
            and position[1] > 1
            and position[2] > 1
            and position[0] < nq.LATTICE_NUM - 2
            and position[1] < nq.LATTICE_NUM - 2
            and position[2] < nq.LATTICE_NUM - 2
        )
        is_out_of_area = not is_out_of_area
        return is_out_of_area