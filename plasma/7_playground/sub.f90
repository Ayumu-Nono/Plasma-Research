program examp2
  implicit none
  real(8) :: r
  real(8) :: V
  real(8) :: pi
  common /pidata/ pi
  pi = acos(-1d0)
  r = 1d0
  call volsub(r,V)
  write(*,*) V
  stop
  end program examp2