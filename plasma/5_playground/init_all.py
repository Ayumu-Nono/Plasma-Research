import numpy as np
import pandas as pd

from initialize.init_calc_area import CalcArea
from initialize.init_particles import NeutralPatricles, IonizedPatricles 


class InitAll:
    def __init__(self, particles_num: int):
        self.area = CalcArea()
        self.neutral = NeutralPatricles(particles_num=particles_num)
        self.ion = IonizedPatricles(particles_num=particles_num)

    def make_calc_area(
        self,
        area_scale: int,
        lattices_scale: int,
        engine_radius: float,
        engine_length: float
    ) -> None:
        self.area.make_lattices(area_scale=area_scale, lattices_scale=lattices_scale)
        self.area.set_engine(radius=engine_radius, length=engine_length)

    def make_particles(self) -> None:
        self.neutral.make_particles()
        self.ion.make_particles()

def main():
    init = InitAll(1000)
    init.make_calc_area(10, 1, 3, 2)
    init.make_particles()
    print(init.ion.particle_list)
    # from result.save import Save
    # save = Save('result/position.csv')
    # for pk in range(len(init.ion.particle_list)):
    #     save.add_row(init.ion.particle_list[pk].position)
    from result.draw import Draw
    draw = Draw('result/position.csv')
    draw.draw()
    

if __name__ == "__main__":
    main()