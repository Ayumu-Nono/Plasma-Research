import sys
import pathlib
import time

import numpy as np
from tqdm import tqdm
from multiprocessing import Pool

root_dir = pathlib.Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from managers.initialize import Initialize
from managers.iterate import Iterate


class Evaluate:

    """"全体フロー(探査機風メソッド名)"""

    def __init__(self, initial_particles_num: int) -> None:
        self.initial_particles_num = initial_particles_num

    def launch(self) -> None:
        print('initializing all in Class "Initialize" ...')    
        self.init = Initialize(particles_num=self.initial_particles_num)
        self.init.init_all()

    def sailing(self) -> None:
        print('iterating in Class "Iterate" ...')
        self.iter = Iterate(init_object=self.init)
        self.iter.iterate()

    def landing(self) -> None:
        print('Outputting in Class "Output" ... ')


def voyage_sequence(particles_num: int) -> None:
    start = time.time()
    e = Evaluate(particles_num)
    e.launch()
    e.sailing()
    e.landing()
    elapsed_time = time.time() - start
    print("Particle number:{0} ".format(particles_num) + "-> {0}[sec]".format(elapsed_time))


if __name__ == "__main__":
    pool_num = 5
    with Pool(pool_num) as p:
        p.map(voyage_sequence, [10, 100, 1000, 10000])
