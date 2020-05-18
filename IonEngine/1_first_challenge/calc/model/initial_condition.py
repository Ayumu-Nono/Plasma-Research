class InitialCondition:
    # field
    potential_of_screengrid: float = 100
    potential_of_vertual_anode: float = 100 # 仮想電極


    # position
    position_of_screengrid: float = 0.5
    position_of_accelgrid: float = 0
    position_of_decelgrid: float = 0.5

    # 微分の際に使う刻み幅
    delta_x = 0.1
