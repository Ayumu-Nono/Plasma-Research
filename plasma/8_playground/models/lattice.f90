module lattice
    implicit none
contains
    function make_lattice_array()
        use numerical_quantity
        implicit none
        real :: make_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM)
        make_lattice_array(:, :) = 0
    end function
end module lattice
