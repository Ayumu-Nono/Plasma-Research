import numpy as np


class Lattices:

    """格子モデル"""

    def __init__(
        self,
        area_scale: float,
        lattice_scale: float,
    ) -> None:
        boundary_layer = 2
        lattices_num = int(area_scale / lattice_scale) + boundary_layer * 2 
        self.lattices = np.zeros((lattices_num, lattices_num, lattices_num))

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
