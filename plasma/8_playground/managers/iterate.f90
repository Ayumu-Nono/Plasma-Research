module iterate
    use numerical_quantity
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
end module iterate