program evaluate
    use numerical_quantity
    use physical_quantity
    use array_debug
    use particle
    use lattice
    use initialize
    use iterate
    implicit none
    integer :: time_step
    call init_all()
    time_step = 1
    call print_2D_array(initial_ion_array)
end program evaluate