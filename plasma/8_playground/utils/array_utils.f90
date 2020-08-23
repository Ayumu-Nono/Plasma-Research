module array_utils
    implicit none
    
contains
    function array_norm(array)
        real, intent(in) :: array(3)
        real :: square_array(3), array_norm
        square_array = array ** 2
        array_norm = SUM(square_array)
        array_norm = sqrt(array_norm)
    end function
end module array_utils
