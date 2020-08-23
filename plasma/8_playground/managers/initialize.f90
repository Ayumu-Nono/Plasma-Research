module initialize
    use numerical_quantity
    implicit none
    
contains
    function init_particles(particle_num)
        integer, intent(in) :: particle_num
        real :: init_particles
        init_particles = 0
    end function
end module initialize