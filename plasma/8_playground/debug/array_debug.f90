module array_debug
    implicit none
    
contains
    subroutine print_2D_array(array)
        implicit none
        integer :: row
        real, intent(in) :: array(:, :)
        do row = 1, size(array(1, :))
            print *, array(:, row)
        end do
    end subroutine

    subroutine print_4D_array(array)
        implicit none
        integer :: y, z
        real, intent(in) :: array(:, :, :, :)
        do z = 1, size(array(1, 1, 1, :))
            do y = 1, size(array(1, 1, :, 1))
                print *, "y=", y, "z=", z
                call print_2D_array(array=array(:, :, y, z))
            end do
        end do
    end subroutine
end module array_debug