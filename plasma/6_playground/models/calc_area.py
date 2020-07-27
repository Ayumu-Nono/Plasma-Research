import numpy as np

from .cells import Cells
from .engine import Engine
from .lattices import Lattices


class CalcArea:
    
    """計算領域"""

    def __init__(
        self,
        cells_num: int,
        engine_radius: float,
        engine_length: float,
        area_scale: float,
        lattice_scale: float,
    ) -> None:
        self.cells = Cells(cells_num=cells_num)
        self.engine = Engine(radius=engine_radius, length=engine_length)
        self.lattices = Lattices(area_scale=area_scale, lattice_scale=lattice_scale)

    def is_in_calc_area(
        self,
        position: np.array
    ) -> bool:
        is_calc_area = (
            not self.engine.is_inner_engine(position=position)
            and not self.lattices.is_out_of_lattices(position=position)
        )
        return is_calc_area


if __name__ == "__main__":
    c = CalcArea(
        cells_num=100,
        engine_radius=3,
        engine_length=4,
        area_scale=100,
        lattice_scale=1
    )
    c.is_in_calc_area(position=np.array([-5,5,5]))
