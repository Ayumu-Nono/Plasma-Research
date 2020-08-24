module electric_potential
    use pic_utils
    use numerical_quantity
    use physical_quantity
    implicit none
contains
    function calc_electric_potential_with_no_collision(ion_density)
        real, intent(in) :: ion_density(LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        real :: calc_electric_potential_with_no_collision(LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
        real :: k, T, e, n0
        k = BOLTZMANN_CONSTANT
        T = ELECTRON_TEMPATATURE
        e = ELEMENTARY_CHARGE
        n0 = PLASMA_DENSITY
        calc_electric_potential_with_no_collision = -k * T / e &
        * log(1+ion_density / n0)
    end function
end module electric_potential