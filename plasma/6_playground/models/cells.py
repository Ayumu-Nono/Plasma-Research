import numpy as np
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models import numerical_quantity as nq


class Cells:

    """Cellモデル"""

    cells: list = [
        [[[] for i3 in range(nq.LATTICE_NUM)] for i2 in range(nq.LATTICE_NUM)]
        for i1 in range(nq.LATTICE_NUM)
    ]

    def save_particles_to_cell(self, particles_list: list,) -> None:
        for particle in particles_list:
            position = particle.position
            position_floor = np.floor(position)
            cell_x = int(position_floor[0])
            cell_y = int(position_floor[1])
            cell_z = int(position_floor[2])
            self.cells[cell_x][cell_y][cell_z].append(particle)
