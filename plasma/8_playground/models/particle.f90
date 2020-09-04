module particle
    use numerical_quantity
    use physical_quantity
    implicit none
    real, PUBLIC :: initial_neutral_array(PARTICLE_MODEL_DIMENSION, INITIAL_NEUTRAL_NUM)
    real, PUBLIC :: initial_ion_array(PARTICLE_MODEL_DIMENSION, INITIAL_ION_NUM)
contains
    subroutine init_particles()
        implicit none
        call init_neutrals()
        call init_ions()
    end subroutine

    subroutine init_neutrals()
        implicit none
        integer :: pk
        initial_neutral_array(1, :) = 1  ! 種類
        initial_neutral_array(2, :) = 0  ! 電荷
        initial_neutral_array(3, :) = XENON_MASS  ! 質量
        do pk = 1, size(initial_neutral_array(1, :))
            ! TODO 乱数発生をコントロール
            call random_number(initial_neutral_array(4:6, pk))
            initial_neutral_array(4:6, pk) = initial_neutral_array(4:6, pk) * 10
            call random_number(initial_neutral_array(7:9, pk))
        end do
    end subroutine

    subroutine init_ions()
        implicit none
        integer :: pk
        initial_ion_array(1, :) = 2  ! 種類
        initial_ion_array(2, :) = ELEMENTARY_CHARGE  ! 電荷
        initial_ion_array(3, :) = XENON_MASS  ! 質量
        do pk = 1, size(initial_ion_array(1, :))
            ! TODO 乱数発生をコントロール
            call random_number(initial_ion_array(4:6, pk))
            initial_ion_array(4:6, pk) = initial_ion_array(4:6, pk) * 10
            call random_number(initial_ion_array(7:9, pk))
        end do
    end subroutine

    function return_initial_cex_particle(position)
        implicit none
        real, intent(in) :: position(3)
        real :: return_initial_cex_particle(PARTICLE_MODEL_DIMENSION)
        return_initial_cex_particle(1) = 3 ! 種類
        return_initial_cex_particle(2) = ELEMENTARY_CHARGE ! 電荷
        return_initial_cex_particle(3) = XENON_MASS ! 質量
        return_initial_cex_particle(4:6) = position
        call random_number(return_initial_cex_particle(7:9))
    end function

    function has_particle_info(a_particle)
        implicit none
        real, intent(in) :: a_particle(PARTICLE_MODEL_DIMENSION)
        logical :: has_particle_info
        if (a_particle(1) == 0) then
            has_particle_info = .false.
        else 
            has_particle_info = .true.
        end if
    end function
end module particle
