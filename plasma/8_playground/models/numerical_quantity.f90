module numerical_quantity
    implicit none
    real, parameter :: STEP_SIZE = 0.001
    integer, parameter :: END_STEP = 10000
    real, parameter :: ENGINE_RADIUS = 3
    real, parameter :: ENGINE_LENGTH = 3 ! [m]
    integer, parameter :: LATTICE_NUM = 100  ! [個]
end module numerical_quantity