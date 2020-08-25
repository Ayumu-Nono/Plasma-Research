module motion
    use physical_quantity
    use array_utils
    implicit none
    
contains
    function righthand_function(velocity, magnetic_field, electric_field)
        real, intent(in) :: velocity(3), magnetic_field(3), electric_field(3)
        real :: righthand_function(3)
        righthand_function = ELEMENTARY_CHARGE &
        * (cross(velocity, magnetic_field) + electric_field) &
        / XENON_MASS
    end function

    function calc_new_velocity(velocity, magnetic_field, electric_field)
        real, intent(in) :: velocity(3), magnetic_field(3), electric_field(3)
        real :: k1(3), k2(3), k3(3), k4(3), h
        real :: calc_new_velocity(3)
        h = STEP_SIZE
        k1 = righthand_function(velocity=velocity, magnetic_field=magnetic_field, electric_field=electric_field)
        k2 = righthand_function(velocity=velocity + (h/2) * k1, magnetic_field=magnetic_field, electric_field=electric_field)
        k3 = righthand_function(velocity=velocity + (h/2) * k2, magnetic_field=magnetic_field, electric_field=electric_field)
        k4 = righthand_function(velocity=velocity + h * k3, magnetic_field=magnetic_field, electric_field=electric_field)
        calc_new_velocity = velocity + (h/6) * (k1+2*k2+2*k3+k4)
    end function

    function calc_new_particle_model(particle, magnetic_field, electric_field)
        real, intent(in) :: particle(PARTICLE_MODEL_DIMENSION), magnetic_field(3), electric_field(3)
        real :: old_x(3), old_v(3), new_x(3), new_v(3), calc_new_particle_model(PARTICLE_MODEL_DIMENSION)
        old_x = particle(4:6)
        old_v = particle(7:9)
        new_v = calc_new_velocity(velocity=old_v, magnetic_field=magnetic_field, electric_field=electric_field)
        new_x = old_x + new_v * STEP_SIZE
        calc_new_particle_model(1:3) = particle(1:3)
        calc_new_particle_model(4:6) = new_x
        calc_new_particle_model(7:9) = new_v
    end function
end module motion