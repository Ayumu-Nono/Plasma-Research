module numerical_quantity
    implicit none
    integer, parameter :: LATTICE_NUM = 100  ! [個]
    integer, parameter :: BOUNDARY = 2  ! [個]
    integer, parameter :: END_STEP = 10000
    integer, parameter :: PARTICLE_MODEL_DIMENSION = 9  !　[種類(0:中性, 1:イオン, 2:CEX), 電荷, 質量, 位置(3D), 速度(3D)]
    integer, parameter :: LATTICE_MODEL_DIMENSION = 4  ! [中性粒子密度, 速度(3D)]
    integer, parameter :: INITIAL_NEUTRAL_NUM = 100  ! [個]
    integer, parameter :: INITIAL_ION_NUM = 100  ! [個]
    real, parameter :: ENGINE_RADIUS = 10  ! 格子の個数分
    real, parameter :: ENGINE_LENGTH = 10  ! 格子の個数分
    real, parameter :: STEP_SIZE = 0.001
end module numerical_quantity