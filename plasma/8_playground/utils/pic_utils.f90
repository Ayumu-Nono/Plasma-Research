module pic_utils
    implicit none
    
contains
    function calc_cube_module(point1, point2)
        implicit none
        real, intent(in) :: point1(3), point2(3)
        real :: dv(3), volume, calc_cube_module
        dv = point1 - point2
        volume = dv(1) * dv(2) * dv(3)
        calc_cube_module = abs(volume)
    end function

    function calc_surrounding_grid(position)
        implicit none
        real, intent(in) :: position(3)
        integer :: position_floor(3), calc_surrounding_grid(8, 3)
        position_floor = int(position)
        calc_surrounding_grid(1, :) = position_floor
        calc_surrounding_grid(2, :) = position_floor + (/1, 0, 0/)
        calc_surrounding_grid(3, :) = position_floor + (/0, 1, 0/)
        calc_surrounding_grid(4, :) = position_floor + (/0, 0, 1/)
        calc_surrounding_grid(5, :) = position_floor + (/1, 1, 0/)
        calc_surrounding_grid(6, :) = position_floor + (/1, 0, 1/)
        calc_surrounding_grid(7, :) = position_floor + (/0, 1, 1/)
        calc_surrounding_grid(8, :) = position_floor + (/1, 1, 1/)
    end function

    function calc_volume_array(position)
        implicit none
        real, intent(in) :: position(3)
        integer :: index
        real :: calc_volume_array(8), grid(8, 3)
        grid = calc_surrounding_grid(position=position)
        if (MINVAL(position) < 0) then
            print *, 'ERROR: Position array contain not positive number.'
            calc_volume_array = 0
        else 
            do index = 1, 8
                calc_volume_array(index) = calc_cube_module( &
                    grid(9 - index, :), &
                    position &
                    )
            end do
        end if
    end function
end module pic_utils