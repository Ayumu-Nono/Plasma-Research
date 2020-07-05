program optional
    call mysub(1,2,3)   ! このように通常通りの利用も可能
    call mysub(1,z=3)   ! このような混在していても可能
    call mysub()        ! すべてを省略した例
    call mysub(z=3,y=2)
  contains
    subroutine mysub(x,y,z)
      integer,optional :: x, y, z    ! optional 属性を付加する
      character*80 line
      if ( present(x) ) then         ! PRESENT の使用例
         print *, "x =", x
      else
         print *, "x is not present..."
      end if
      if ( present(y) ) then
         print *, "y =", y
      else
         print *, "y is not present..."
      end if
      if ( present(z) ) then
         print *, "z =", z
      else
         print *, "z is not present..."
      end if
      print *
    end subroutine
  end program
  