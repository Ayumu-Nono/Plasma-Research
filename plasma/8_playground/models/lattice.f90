module lattice
    use numerical_quantity
    use array_utils
    implicit none
    real :: neutral_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    real :: ion_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    real :: cex_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
contains
    subroutine init_lattice()
        neutral_lattice_array = 0
        ion_lattice_array = 0
        cex_lattice_array = 0
    end subroutine

    function is_in_calc_area(position)
        real, intent(in) :: position(3)
        logical :: is_in_calc_area
        is_in_calc_area = ( &
            (.not. is_inner_engine(position=position)) &
            .and. &
            (is_inside_of_boundary(position=position)) &
        )
    end function

    function is_inside_of_boundary(position)
        implicit none
        real ,intent(in) :: position(3)
        logical :: is_inside_of_boundary
        is_inside_of_boundary = ( &
            position(1) > BOUNDARY &
            .and. position(2) > BOUNDARY &
            .and. position(3) > BOUNDARY &
            .and. position(1) <= LATTICE_NUM - BOUNDARY &
            .and. position(2) <= LATTICE_NUM - BOUNDARY &
            .and. position(3) <= LATTICE_NUM - BOUNDARY &
        )
    end function

    function is_inner_engine(position)
        implicit none
        real, intent(in) :: position(3)
        real :: delta_array(3), norm
        logical :: is_inner_engine
        delta_array = (/ 0.0, position(2), position(3) /)
        norm = array_norm(array=delta_array)
        is_inner_engine = (norm < ENGINE_RADIUS) .and. (position(1) < ENGINE_LENGTH)
    end function

end module lattice
