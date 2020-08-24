module density
    use pic_utils
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
end module density