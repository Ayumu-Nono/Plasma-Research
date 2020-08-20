module lattice
    use numerical_quantity
    implicit none
    real :: lattice_array(4, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM) = 0
contains
    subroutine print_lattice_array()
        print *, "density   velocity_x  velocity_y  velocity_z"
        print *, lattice_array(:, 1, 1, 1)
    end subroutine print_lattice_array

end module lattice