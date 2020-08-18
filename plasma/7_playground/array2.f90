program array_2d
    implicit none
    real :: a(2,3,4)
    a = 1
    print *, a(:,2,2)
end program array_2d
