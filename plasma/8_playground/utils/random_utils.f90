module random_utils
    implicit none
contains
    function round_with_bias(hoge)
        implicit none
        real, intent(in) :: hoge
        real :: decimal_part, x, round_with_bias
        decimal_part = hoge - int(hoge)
        call random_number(x)
        if (x > decimal_part) then
            round_with_bias = hoge
        else
            round_with_bias = hoge + 1.0
        end if
    end function
end module random_utils