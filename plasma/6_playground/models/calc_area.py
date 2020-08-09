import numpy as np
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models.engine import Engine
from models.lattices import Lattices


class CalcArea(Engine, Lattices):

    """計算領域"""

    def __init__(self) -> None:
        self.lattice_for_neutral = Lattices(lattice_type="neutral")
        self.lattice_for_ion = Lattices(lattice_type="ion")
        self.lattice_for_CEX = Lattices(lattice_type="CEX")

    def is_in_calc_area(
        self,
        position: np.array
    ) -> bool:
        is_calc_area = (
            not self.is_inner_engine(position=position)
            and not self.is_out_of_lattices(position=position)
        )
        return is_calc_area


if __name__ == "__main__":
    c = CalcArea()
    print(c.lattice_for_neutral.density + c.lattice_for_neutral.density)
