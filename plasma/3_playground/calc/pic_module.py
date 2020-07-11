import numpy as np


class PICModule:

    """PICに使うモジュール"""

    def calc_cube_volume(
        self,
        point1: np.array,
        point2: np.array
    ) -> float:
        dv = np.abs(point2 - point1)
        volume = dv[0] * dv[1] * dv[2]
        return volume

    def calc_surrounding_grid(
        self,
        position: np.array
    ) -> np.array:
        position_floor = np.floor(position).astype(np.int64)  # キャストしてるところ。桁落ちなど注意。
        grid_x0_y0_z0 = position_floor
        grid_x1_y0_z0 = position_floor + np.array([1, 0, 0], dtype=np.int64)
        grid_x0_y1_z0 = position_floor + np.array([0, 1, 0], dtype=np.int64)
        grid_x0_y0_z1 = position_floor + np.array([0, 0, 1], dtype=np.int64)
        grid_x1_y1_z0 = position_floor + np.array([1, 1, 0], dtype=np.int64)
        grid_x1_y0_z1 = position_floor + np.array([1, 0, 1], dtype=np.int64)
        grid_x0_y1_z1 = position_floor + np.array([0, 1, 1], dtype=np.int64)
        grid_x1_y1_z1 = position_floor + np.array([1, 1, 1], dtype=np.int64)
        grid_array = np.array([
            grid_x0_y0_z0,
            grid_x1_y0_z0,
            grid_x0_y1_z0,
            grid_x0_y0_z1,
            grid_x1_y1_z0,
            grid_x1_y0_z1,
            grid_x0_y1_z1,
            grid_x1_y1_z1
        ])
        return grid_array

    def calc_volume_array(
        self,
        position: np.array
    ) -> np.array:
        if not np.all(position > 0):
            print('ERROR: Position array contain not positive number.')
            raise KeyboardInterrupt
        position_floor = np.floor(position).astype(np.int64)
        grid_x0_y0_z0 = position_floor
        grid_x1_y0_z0 = position_floor + np.array([1, 0, 0], dtype=np.int64)
        grid_x0_y1_z0 = position_floor + np.array([0, 1, 0], dtype=np.int64)
        grid_x0_y0_z1 = position_floor + np.array([0, 0, 1], dtype=np.int64)
        grid_x1_y1_z0 = position_floor + np.array([1, 1, 0], dtype=np.int64)
        grid_x1_y0_z1 = position_floor + np.array([1, 0, 1], dtype=np.int64)
        grid_x0_y1_z1 = position_floor + np.array([0, 1, 1], dtype=np.int64)
        grid_x1_y1_z1 = position_floor + np.array([1, 1, 1], dtype=np.int64)
        volume_x0_y0_z0 = self.calc_cube_volume(grid_x0_y0_z0, position)
        volume_x1_y0_z0 = self.calc_cube_volume(grid_x1_y0_z0, position)
        volume_x0_y1_z0 = self.calc_cube_volume(grid_x0_y1_z0, position)
        volume_x0_y0_z1 = self.calc_cube_volume(grid_x0_y0_z1, position)
        volume_x1_y1_z0 = self.calc_cube_volume(grid_x1_y1_z0, position)
        volume_x1_y0_z1 = self.calc_cube_volume(grid_x1_y0_z1, position)
        volume_x0_y1_z1 = self.calc_cube_volume(grid_x0_y1_z1, position)
        volume_x1_y1_z1 = self.calc_cube_volume(grid_x1_y1_z1, position)
        volume_array = np.array([
            volume_x0_y0_z0,
            volume_x1_y0_z0,
            volume_x0_y1_z0,
            volume_x0_y0_z1,
            volume_x1_y1_z0,
            volume_x1_y0_z1,
            volume_x0_y1_z1,
            volume_x1_y1_z1
        ])
        if not np.sum(volume_array) == 1:
            print('Volume sum not equal 1')
            raise KeyboardInterrupt
        # 逆順にすることを忘れずに
        volume_array = volume_array[::-1]
        return volume_array


def main():
    p = PICModule()
    print(p.calc_volume_array(np.array([1,2,3.3])))
    


if __name__ == "__main__":
    main()