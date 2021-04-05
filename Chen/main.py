from tqdm import tqdm
from typing import List
import numpy as np
import pandas as pd

from world import Lattice, World
from particle import Particle
from draw import make_figure


p = Particle(
    mass=1, charge=1, initial_p=np.array([1, 1, 1]), initial_v=np.array([1, 0, 0])
)
world = World()


results: list = []
for t in tqdm(range(5000)):
    # set field ##################
    x = p.position[0]
    y = p.position[1]
    z = p.position[2]
    r = (x **2 + y **2) ** (-1 /2)
    theta = np.arctan(y / x)
    world.set_field(efield=[0, 0, 0], mfield=[0, r * np.cos(theta), r * np.sin(theta)])
    #######################
    efield = world.field.efield
    mfield = world.field.mfield
    p.update(efield=efield, mfield=mfield, timestep=0.01)
    result: dict = {
        "t": t,
        "position_x": p.position[0],
        "position_y": p.position[1],
        "position_z": p.position[2],
        "velocity": np.linalg.norm(p.velocity),
    }
    results.append(result)

df = pd.DataFrame(results)
df.to_csv("result.csv")

make_figure("E=0By=rcos(theta)Bz=rsin(theta).png")
