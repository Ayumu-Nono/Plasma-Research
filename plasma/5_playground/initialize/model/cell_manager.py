import numpy as np


class CellManager:

    """"Cellをコントロールするクラス"""

    def __init__(self, cells: np.array) -> None:
        self.cells = cells

    def init_cells(self) -> None:
        for i in range(10):
            for j in range(10):
                for k in range(10):
                    self.cells[i, j, k] = 

    def save_particles_to_cell(
        self,
        particles_list: list,
    ) -> None:
        cells_num = len(self.cells)
        i = 0
        j = 0
        k = 0
        # self.cells = 


if __name__ == "__main__":
    cell_manager = CellManager(np.zeros((10, 10, 10)))
    cell_manager.init_cells()
