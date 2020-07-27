import numpy as np
import pathlib
import sys

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from models import numerical_quantity as nq


class Engine:

    """エンジンモデル"""

    radius = nq.ENGINE_RADIUS
    length = nq.ENGINE_LENGTH

    def is_inner_engine(
        self,
        position: np.array,
    ) -> bool:
        position_x = position[0]
        delta_array = position - np.array([position_x, 0, 0])
        norm = np.linalg.norm(delta_array)
        is_inner_engine = (norm < self.radius) and (position_x < self.length)
        return is_inner_engine
