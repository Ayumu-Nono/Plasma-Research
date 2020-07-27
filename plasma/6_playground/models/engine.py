import numpy as np


class Engine:

    """エンジンモデル"""

    def __init__(
        self,
        radius: float,
        length:float,
    ) -> None:
        self.radius = radius
        self.length = length

    def is_inner_engine(
        self,
        position: np.array,
    ) -> bool:
        position_x = position[0]
        delta_array = position - np.array([position_x, 0, 0])
        norm = np.linalg.norm(delta_array)
        is_inner_engine = (norm < self.radius) and (position_x < self.length)
        return is_inner_engine
