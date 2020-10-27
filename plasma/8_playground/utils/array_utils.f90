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

    function cross(array1, array2)
        real, intent(in) :: array1(3), array2(3)
        real :: cross(3)
        cross(1) = array1(2) * array2(3) - array1(3) * array2(2)
        cross(2) = array1(3) * array2(1) - array1(1) * array2(3)
        cross(3) = array1(1) * array2(2) - array1(2) * array2(1)
    end function
end module array_utils
