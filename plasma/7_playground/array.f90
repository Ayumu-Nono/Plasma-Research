program array_2d
    implicit none
    real :: a(5,5,5)
    a = 10
    call print_as_matrix(a, 5)
end program array_2d

subroutine print_as_matrix(array, array_size)
    implicit none
    integer :: x, y, z
    integer :: array_size
    real :: array(array_size, array_size, array_size)
    do z=1,array_size
        print *, "z=", z
        do y=1,array_size
            do x=1,array_size
                write (*, fmt='(f15.4)', advance='no') array(x, y, z)
            enddo
            print *, ""
        enddo
    enddo
end subroutine