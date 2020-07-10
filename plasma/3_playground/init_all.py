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
        era_scale: int,
        latice_scale: int,
        engine_radius: float,
        engine_length: float
    ) -> None:
        self.area.make_latice(era_scale=era_scale, latice_scale=latice_scale)
        self.area.set_engine(radius=engine_radius, length=engine_length)

def main():
    init = InitAll(10)
    init.make_calc_area(10, 1, 3, 2)


if __name__ == "__main__":
    main()