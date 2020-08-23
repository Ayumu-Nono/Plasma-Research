module lattice
    use numerical_quantity
    implicit none
contains
    function make_lattice_array()
        implicit none
        real :: make_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM)
        make_lattice_array(:, :) = 0
    end function
end module lattice
