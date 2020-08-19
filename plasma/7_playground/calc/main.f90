subroutine volsub(r,V)
    real(8), intent(in) :: r
    real(8) :: pi
    real(8), intent(inout) :: V
    common /pidata/ pi
    V = 4d0/3d0*pi*r**3
    end subroutine volsub