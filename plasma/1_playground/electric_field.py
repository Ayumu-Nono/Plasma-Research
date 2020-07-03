import numpy as np
import math

class ElectricFieldModel:
    def __init__(
        self,
    ):
        pass

    def set_electric_potential(
        self,
        cell_num: int 
    ) -> None:
        potential = np.random.rand(cell_num ** 3).reshape(cell_num, cell_num, cell_num) * 10
        self.electric_potential = potential

    def calc_electric_field_on_grid(
        self,
        position: np.array
    ) -> np.array:
        x = int(position[0])
        y = int(position[1])
        z = int(position[2])
        potential = self.electric_potential
        field_x = potential[x + 1][y][z] - potential[x][y][z] 
        field_y = potential[x][y + 1][z] - potential[x][y][z]
        field_z = potential[x][y][z + 1] - potential[x][y][z]
        # WARNING: Never forget to append "-"
        return - np.array([field_x, field_y, field_z])

    def calc_cube_volume(
        self,
        point1: np.array,
        point2: np.array
    ) -> float:
        dv = np.abs(point2 - point1)
        volume = dv[0] * dv[1] * dv[2]
        return volume

    def calc_electric_field_on_free_point(
        self,
        position: np.array
    ) -> np.array:
        position_floor = np.floor(position).astype(np.int64)
        position_ceil = np.ceil(position).astype(np.int64)
        grid_x0_y0_z0 = position_floor
        grid_x1_y0_z0 = position_floor + np.array([1, 0, 0], dtype=np.int64)
        grid_x0_y1_z0 = position_floor + np.array([0, 1, 0], dtype=np.int64)
        grid_x0_y0_z1 = position_floor + np.array([0, 0, 1], dtype=np.int64)
        grid_x1_y1_z0 = position_floor + np.array([1, 1, 0], dtype=np.int64)
        grid_x1_y0_z1 = position_floor + np.array([1, 0, 1], dtype=np.int64)
        grid_x0_y1_z1 = position_floor + np.array([0, 1, 1], dtype=np.int64)
        grid_x1_y1_z1 = position_ceil
        volume_x0_y0_z0 = self.calc_cube_volume(grid_x0_y0_z0, position)
        volume_x1_y0_z0 = self.calc_cube_volume(grid_x1_y0_z0, position)
        volume_x0_y1_z0 = self.calc_cube_volume(grid_x0_y1_z0, position)
        volume_x0_y0_z1 = self.calc_cube_volume(grid_x0_y0_z1, position)
        volume_x1_y1_z0 = self.calc_cube_volume(grid_x1_y1_z0, position)
        volume_x1_y0_z1 = self.calc_cube_volume(grid_x1_y0_z1, position)
        volume_x0_y1_z1 = self.calc_cube_volume(grid_x0_y1_z1, position)
        volume_x1_y1_z1 = self.calc_cube_volume(grid_x1_y1_z1, position)
        electric_field = self.calc_electric_field_on_grid(grid_x0_y0_z0) * volume_x1_y1_z1 \
            + self.calc_electric_field_on_grid(grid_x1_y0_z0) * volume_x0_y1_z1 \
            + self.calc_electric_field_on_grid(grid_x0_y1_z0) * volume_x1_y0_z1 \
            + self.calc_electric_field_on_grid(grid_x0_y0_z1) * volume_x1_y1_z0 \
            + self.calc_electric_field_on_grid(grid_x1_y1_z0) * volume_x0_y0_z1 \
            + self.calc_electric_field_on_grid(grid_x1_y0_z1) * volume_x0_y1_z0 \
            + self.calc_electric_field_on_grid(grid_x0_y1_z1) * volume_x1_y0_z0 \
            + self.calc_electric_field_on_grid(grid_x1_y1_z1) * volume_x0_y0_z0 
        return electric_field


    
def main():
    field = ElectricFieldModel()
    field.set_electric_potential(10)
    field.calc_electric_field_on_free_point(np.array([3.2, 4.5, 5.1]))


if __name__ == "__main__":
    main()