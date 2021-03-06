module numerical_quantity
    implicit none
    integer, parameter :: LATTICE_NUM = 100  ! [個]
    ! TODO　粒子ひとつあたりに、現実世界の粒子何個分に相当させるか考える
    integer, parameter :: PARTICLE_MAGNIFICATION = 100  ! [個]
    integer, parameter :: BOUNDARY = 2  ! [個]
    integer, parameter :: END_STEP = 3 ! [回]
    integer, parameter :: PARTICLE_MODEL_DIMENSION = 9  !　[種類(1:中性, 2:イオン, 3:CEX), 電荷, 質量, 位置(3D), 速度(3D)]
    integer, parameter :: LATTICE_MODEL_DIMENSION = 4  ! [粒子密度, 速度(3D)]
    integer, parameter :: INITIAL_NEUTRAL_NUM = 10000  ! [個]
    integer, parameter :: INITIAL_ION_NUM = 100  ! [個]
    integer, parameter :: ITERATE_NEUTRAL_NUM = INITIAL_NEUTRAL_NUM  ! [個]
    integer, parameter :: ITERATE_ION_NUM = INITIAL_ION_NUM  ! [個]
    integer, parameter :: ITERATE_CEX_NUM = INITIAL_ION_NUM  ! [個]
    real, parameter :: ENGINE_RADIUS = 10  ! 格子の個数分
    real, parameter :: ENGINE_LENGTH = 10  ! 格子の個数分
    real, parameter :: STEP_SIZE = 0.1 ! [s]
end module numerical_quantity