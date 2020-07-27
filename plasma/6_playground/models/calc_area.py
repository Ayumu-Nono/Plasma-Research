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
        pass

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
    print(c.is_in_calc_area(position=np.array([5,5,5])))
