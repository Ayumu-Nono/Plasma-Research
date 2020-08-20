module particle
    implicit none
contains
    subroutine make_particle_array(particle_num)
        integer particle_num
        real :: particle_array(5) = 0
        print *, particle_num
        print *, particle_array(:)
    end subroutine make_particle_array
end module particle