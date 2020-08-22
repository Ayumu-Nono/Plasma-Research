module array
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
end module array