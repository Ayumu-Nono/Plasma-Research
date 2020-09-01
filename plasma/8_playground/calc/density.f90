module density
    use pic_utils
    use numerical_quantity
    implicit none
contains
    function calc_density_array(position)
        implicit none
        real, intent(in) :: position(3)
        integer :: grid
        real :: surrounding_grid(3, 8), volume_array(8)
        real :: calc_density_array(4, 8)
        surrounding_grid = calc_surrounding_grid(position=position)
        volume_array = calc_volume_array(position=position)
        do grid = 1, 8
            calc_density_array(1:3, grid) = surrounding_grid(:, grid)
            calc_density_array(4, grid) = volume_array(grid)
        end do
    end function

    function calc_new_lattice_with_density_info(density_array, lattice_array)
        implicit none
        real, intent(in) :: density_array(4, 8)
        real, intent(in) :: lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        real :: calc_new_lattice_with_density_info(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        integer :: grid
        calc_new_lattice_with_density_info = lattice_array
        do grid = 1, 8
            calc_new_lattice_with_density_info( &
            1, &
            int(density_array(1, grid)), &
            int(density_array(2, grid)), &
            int(density_array(3, grid)) &
            ) = &
            calc_new_lattice_with_density_info( &
            1, &
            int(density_array(1, grid)), &
            int(density_array(2, grid)), &
            int(density_array(3, grid)) &
            ) &
            + density_array(4, grid)
        end do
    end function
end module density