program array_append
    implicit none
    real, allocatable :: a(:,:)
    real :: b(2) = 2
    a = [real ::][real ::]
    print *, a
    a = [a, b]
    print *, a
    
end program array_append