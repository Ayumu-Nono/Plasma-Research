module particle
    implicit none
contains
    function make_particle_array(particle_num)
        use numerical_quantity
        implicit none
        integer, intent(in) :: particle_num
        real :: make_particle_array(PARTICLE_MODEL_DIMENSION, particle_num)
        make_particle_array(:, :) = 0
    end function
end module particle
