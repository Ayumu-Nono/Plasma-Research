import numpy as np
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models import numerical_quantity as nq


class Lattices:

    """格子モデル"""
    lattices = np.zeros((nq.LATTICE_NUM, nq.LATTICE_NUM, nq.LATTICE_NUM))

    def is_out_of_lattices(
        self,
        position: np.array
    ) -> bool:
        is_out_of_area = (
            position[0] > 1
            and position[1] > 1
            and position[2] > 1
            and position[0] < len(self.lattices) - 2
            and position[1] < len(self.lattices) - 2
            and position[2] < len(self.lattices) - 2
        )
        is_out_of_area = not is_out_of_area
        return is_out_of_area
