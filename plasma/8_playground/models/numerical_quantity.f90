module numerical_quantity
    implicit none
    integer, parameter :: LATTICE_NUM = 100  ! [個]
    integer, parameter :: END_STEP = 10000
    integer, parameter :: INITIAL_PARTICLE_NUM = 1d3  ! [個]
    real, parameter :: ENGINE_RADIUS = 3
    real, parameter :: ENGINE_LENGTH = 3 ! [m]
    real, parameter :: STEP_SIZE = 0.001
end module numerical_quantity