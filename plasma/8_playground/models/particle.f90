module particle
    implicit none
contains
    function make_particle_array(particle_num)
        implicit none
        integer, intent(in) :: particle_num
        real :: make_particle_array(particle_num)
        make_particle_array(:) = 0
    end function

    ! subroutine make_particle_array(particle_num)
    !     implicit none
    !     integer, intent(in) :: particle_num
    !     real, intent(out) :: return_array
    !     real :: particle_array(particle_num)
    !     print *, particle_num
    !     print *, particle_array(:)
    ! end subroutine make_particle_array
end module particle

! TODO: 返り値に配列