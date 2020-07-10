import numpy as np


class PICModule:
    def calc_cube_volume(
        self,
        point1: np.array,
        point2: np.array
    ) -> float:
        dv = np.abs(point2 - point1)
        volume = dv[0] * dv[1] * dv[2]
        return volume

