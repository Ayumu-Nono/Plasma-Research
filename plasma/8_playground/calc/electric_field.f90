module calc_electric_field
    use pic_utils
    use numerical_quantity
    use physical_quantity
    implicit none
    real :: electric_potential(LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    ! real :: electric_field(3, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
contains
    subroutine calc_electric_potential_with_no_collision(ion_density)
        implicit none
        real, intent(in) :: ion_density(LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        real :: k, T, e, n0
        k = BOLTZMANN_CONSTANT
        T = ELECTRON_TEMPATATURE
        e = ELEMENTARY_CHARGE
        n0 = PLASMA_DENSITY
        electric_potential = -k * T / e &
        * log(1+ion_density / n0)
    end subroutine

    function calc_electric_field_on_grid(position)
        implicit none
        real, intent(in) :: position(3)
        integer :: x, y, z
        real :: calc_electric_field_on_grid(3)
        x = int(position(1))
        y = int(position(2))
        z = int(position(3))
        calc_electric_field_on_grid(1) = electric_potential(x+1, y, z) - electric_potential(x, y, z)
        calc_electric_field_on_grid(2) = electric_potential(x, y+1, z) - electric_potential(x, y, z)
        calc_electric_field_on_grid(3) = electric_potential(x, y, z+1) - electric_potential(x, y, z)
    end function

    function calc_electric_field_on_free_point(position)
        implicit none
        real, intent(in) :: position(3)
        real :: volume_ratio_array(8), surrounding_grid_array(3, 8)
        real :: calc_electric_field_on_free_point(3)
        integer :: grid
        volume_ratio_array = calc_volume_array(position=position)
        surrounding_grid_array = calc_surrounding_grid(position=position)
        calc_electric_field_on_free_point = 0
        do grid = 1, 8
            calc_electric_field_on_free_point(:) += calc_electric_field_on_grid(surrounding_grid_array(:, grid)) &
            * volume_ratio_array(grid)
        end do
    end function
end module calc_electric_field