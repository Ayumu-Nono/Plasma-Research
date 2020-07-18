import numpy as np

from model.cell_manager import CellManager


class CalcArea:

    """境界条件・計算領域内判定"""
    
    def make_lattices(
        self,
        area_scale: int,
        lattices_scale: int,
    ) -> None:
        boundary_layer = 2
        lattices_num = int(area_scale / lattices_scale) + boundary_layer * 2 
        self.lattices = np.zeros((lattices_num, lattices_num, lattices_num))
    
    def make_cells(
        self,
        area_scale: int,
        cells_scale: int,
    ) -> None:
        boundary_layer = 2
        cells_num = int(area_scale / cells_scale) + boundary_layer * 2
        self.cell_manager = CellManager(cells_num=cells_num)
        print(self.cell_manager.cells)

    def set_engine(
        self,
        radius: float,
        length: float,
    ) -> None:
        self.engine_radius = radius
        self.engine_length = length

    def is_inner_engine(
        self,
        position: np.array,
    ) -> bool:
        position_x = position[0]
        delta_array = position - np.array([position_x, 0, 0])
        norm = np.linalg.norm(delta_array)
        is_inner_engine = (norm < self.engine_radius) and (position_x < self.engine_length)
        return is_inner_engine
    
    def is_out_of_area(
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
        
    def is_in_calc_area(
        self,
        position: np.array
    ) -> bool:
        is_calc_area = (
            not self.is_inner_engine(position=position)
            and not self.is_out_of_area(position=position) 
        )
        return is_calc_area

    def test(self):
        self.make_cells(10, 1)
        self.make_lattices(10,1)
        self.set_engine(radius=5.1, length=2)

def main():
    init = CalcArea()
    init.test()


if __name__ == "__main__":
    main()