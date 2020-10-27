program sum
    implicit none
    integer total, i, j, num
    total = 0
    num = 10000
    do i = 1, num
        do j = 1, num
            total = total + i
        enddo
    end do
    print *, total
  end program sum
  