module iterate
    use numerical_quantity
    use particle
    use lattice
    use calc_electric_field
    use density
    use motion
    use array_debug
    implicit none
    real, PUBLIC :: neutral_array(PARTICLE_MODEL_DIMENSION, INITIAL_NEUTRAL_NUM)
    real, PUBLIC :: ion_array(PARTICLE_MODEL_DIMENSION, INITIAL_ION_NUM)
    real :: neutral_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    real :: ion_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    real :: cex_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
contains
    subroutine each_step()
        implicit none
        
    end subroutine

    subroutine receive_info_from_initializer()
        implicit none
        neutral_array = initial_neutral_array
        ion_array = initial_ion_array
        neutral_lattice_array = initial_neutral_lattice_array
        ion_lattice_array = initial_ion_lattice_array
    end subroutine
end module iterate