module velocity_sum
    use pic_utils
    use numerical_quantity
    implicit none
contains
    function calc_velocity_sum_array(a_particle)
        real, intent(in) :: a_particle(PARTICLE_MODEL_DIMENSION)
        integer :: grid
        real :: surrounding_grid(3, 8), volume_array(8)
        real :: calc_velocity_sum_array(6, 8) ! [surrounding_grid(3D), volume_array(3D)]
        surrounding_grid = calc_surrounding_grid(position=a_particle(4:6))
        volume_array = calc_volume_array(position=a_particle(4:6))
        do grid = 1, 8
            calc_velocity_sum_array(1:3, grid) = surrounding_grid(:, grid)
            calc_velocity_sum_array(4:6, grid) = volume_array(grid) * a_particle(7:9)
        end do
    end function
    
    function calc_new_lattice_with_velocity_sum_info(velocity_sum_array, lattice_array)
        implicit none
        real, intent(in) :: velocity_sum_array(6, 8)
        real, intent(in) :: lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        real :: calc_new_lattice_with_velocity_sum_info(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        integer :: grid
        calc_new_lattice_with_velocity_sum_info = lattice_array
        do grid = 1, 8
            calc_new_lattice_with_velocity_sum_info( &
            2:4, &
            int(velocity_sum_array(1, grid)), &
            int(velocity_sum_array(2, grid)), &
            int(velocity_sum_array(3, grid)) &
            ) = &
            calc_new_lattice_with_velocity_sum_info( &
            2:4, &
            int(velocity_sum_array(1, grid)), &
            int(velocity_sum_array(2, grid)), &
            int(velocity_sum_array(3, grid)) &
            ) &
            + velocity_sum_array(4:6, grid)
        end do
    end function

end module velocity_sum