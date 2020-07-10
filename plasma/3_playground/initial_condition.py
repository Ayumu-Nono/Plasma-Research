import numpy as np


class InitialCondition:
    def make_latice(
        self,
        era_scale: int,
        latice_scale: int,
    ) -> None:
        boundary_layer = 0  # やっぱこれいらないから０にしとく
        latice_num = int(era_scale / latice_scale) + boundary_layer * 2 
        self.latice = np.zeros((latice_num, latice_num, latice_num))
        print(len(self.latice))

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
    
    def is_outer_erea(
        self,
        position: np.array
    ) -> bool:
        is_outer_erea = (
            position[0] > 0
            and position[1] > 0
            and position[2] > 0
            and position[0] < len(self.latice)
            and position[1] < len(self.latice)
            and position[2] < len(self.latice)
        )
        is_outer_erea = not is_outer_erea
        return is_outer_erea
        
    def is_calc_erea(
        self,
        position: np.array
    ) -> bool:
        is_calc_erea = (
            not self.is_inner_engine
            and not self.is_outer_erea 
        )
        return is_calc_erea

    def test(self):
        self.make_latice(10,1)
        self.set_engine(radius=5.1, length=2)
        self.is_inner_engine(np.array([1, 3, 4]))
        self.is_outer_erea(np.array([100,1,1]))


def main():
    init = InitialCondition()
    init.test()


if __name__ == "__main__":
    main()