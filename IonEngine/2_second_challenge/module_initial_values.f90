! 初期条件
module initial_condition
    ! field
    real,parameter :: potential_of_screengrid = 100
    ! position
    real,parameter :: position_of_screengrid = -10
    real,parameter :: position_of_accelgrid = 0
    ! diffusion
    real,parameter :: delta_x = 0.001

end module initial_condition

! 物理量
module physical_quantity
    ! particle
    real,parameter :: electron_charge = -1.602E-19
    real,parameter :: electron_mass = 9.10938356E-31

    ! permittivity(誘電率)
    real,parameter :: vaccum_permittivity = 8.8541878128E-12

end module physical_quantity