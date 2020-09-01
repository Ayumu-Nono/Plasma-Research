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
    call receive_info_from_initializer()
    time_step = 1
    call each_step()
    call print_2D_array(ion_array)
end program evaluate