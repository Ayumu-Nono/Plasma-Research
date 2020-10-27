module charge_exchange
    use pic_utils
    use random_utils
    use numerical_quantity
    use physical_quantity
    implicit none
contains
    function calc_generate_rate_on_grid( &
        neutral_density, &
        ion_density, & 
        neutral_velocity, &
        ion_velocity &
    )
        implicit none
        real, intent(in) :: neutral_density, ion_density
        real, intent(in) :: neutral_velocity, ion_velocity
        real :: kinetic_energy, cross_section
        real :: calc_generate_rate_on_grid
        kinetic_energy = (1/2) * XENON_MASS * ion_velocity ** 2
        cross_section = 87.3 -13.6 * log(1+kinetic_energy)
        calc_generate_rate_on_grid = neutral_density * ion_density &
            * neutral_velocity * cross_section
    end function

    function calc_velocity_norm(velocity_array)
        implicit none
        real, intent(in) :: velocity_array(3)
        real :: calc_velocity_norm
        calc_velocity_norm = velocity_array(1)**2 + velocity_array(2)**2 + velocity_array(3)**2
        calc_velocity_norm = sqrt(calc_velocity_norm)
    end function

    function calc_average_velocity(a_lattice)
        implicit none
        real, intent(in) :: a_lattice(LATTICE_MODEL_DIMENSION)
        real :: calc_average_velocity
        real :: velocity_norm
        velocity_norm = calc_velocity_norm(velocity_array=a_lattice(2:4))
        if (a_lattice(1) > 0.01) then
            calc_average_velocity = velocity_norm / a_lattice(1)
        else
            calc_average_velocity = 0
        end if
    end function
    
end module charge_exchange