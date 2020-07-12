import numpy as np


class CalcArea:

    """境界条件・計算領域内判定"""
    
    def make_latice(
        self,
        era_scale: int,
        latice_scale: int,
    ) -> None:
        boundary_layer = 2
        latice_num = int(era_scale / latice_scale) + boundary_layer * 2 
        self.latice = np.zeros((latice_num, latice_num, latice_num))

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
            position[0] < 1
            and position[1] < 1
            and position[2] < 1
            and position[0] > len(self.latice) - 2
            and position[1] > len(self.latice) - 2
            and position[2] > len(self.latice) - 2
        )
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
        self.make_latice(10,1)
        self.set_engine(radius=5.1, length=2)

def main():
    init = CalcArea()
    init.test()


if __name__ == "__main__":
    main()