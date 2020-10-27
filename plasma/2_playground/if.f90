program if
    implicit none
    integer a, b
    print *, "Please enter two numbers:"
    read *, a, b
    if ( a > b ) then
      print *, "a is greator than b!"
    else if ( a == b ) then
      print *, "a is equal to b!"
    else
      print *, "a is less than b!"
    end if
  end program if