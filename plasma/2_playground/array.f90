program array_2d
    implicit none
    integer :: a(2,2), b(2,2)
    a(1,1) = 1
    a(2,1) = 20
    a(1,2) = 30
    a(2,2) = 40
    b(:, :) = 1
    print *, a * b
end program array_2d