module calc_field

contains

    function calcDeform(y) result (w)

        real, intent(in) :: y 
        real w
        
        w = y**2
        
    end function calcDeform

end module calc_field