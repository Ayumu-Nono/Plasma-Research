import numpy as np


class Cells:

    """Cellモデル"""

    def __init__(self, cells_num: int) -> None:
        self.cells = [[[[] for i3 in range(cells_num)] for i2 in range(cells_num)] for i1 in range(cells_num)]

    def save_particles_to_cell(
        self,
        particles_list: list,
    ) -> None:
        for particle in particles_list:
            position = particle.position
            position_floor = np.floor(position)
            cell_x = int(position_floor[0])
            cell_y = int(position_floor[1])
            cell_z = int(position_floor[2])
            self.cells[cell_x][cell_y][cell_z].append(particle)    
