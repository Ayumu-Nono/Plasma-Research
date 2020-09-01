module iterate
    use numerical_quantity
    use particle
    use lattice
    use calc_electric_field
    use density
    use motion
    use array_debug
    implicit none
    real, PUBLIC :: neutral_array(PARTICLE_MODEL_DIMENSION, ITERATE_NEUTRAL_NUM)
    real, PUBLIC :: ion_array(PARTICLE_MODEL_DIMENSION, ITERATE_ION_NUM)
    real, PUBLIC :: cex_array(PARTICLE_MODEL_DIMENSION, ITERATE_ION_NUM)
    real :: neutral_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    real :: ion_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
    real :: cex_lattice_array(LATTICE_MODEL_DIMENSION, LATTICE_NUM, LATTICE_NUM, LATTICE_NUM)
contains
    subroutine each_step()
        implicit none
        call delete_particle_out_of_calc_area()
        call align_particle_array()
        call push_particle_info_to_grid()
        call calc_field()
        call print_3D_array(electric_potential)
        ! call print_4D_array(neutral_lattice_array)
    end subroutine

    subroutine calc_field()
        call calc_electric_potential_with_no_collision(ion_density=ion_lattice_array(1, :, :, :))
        print *, electric_potential
    end subroutine

    subroutine receive_info_from_initializer()
        implicit none
        neutral_array(:, 1:INITIAL_NEUTRAL_NUM) = initial_neutral_array
        ion_array(:, 1:INITIAL_ION_NUM) = initial_ion_array
        neutral_lattice_array = initial_neutral_lattice_array
        ion_lattice_array = initial_ion_lattice_array
    end subroutine

    subroutine push_particle_info_to_grid()
        implicit none
        integer :: pk
        real :: a_particle(PARTICLE_MODEL_DIMENSION), position(3), density_array(4, 8)
        do pk = 1, size(neutral_array(1, :))
            a_particle = neutral_array(:, pk)
            if (has_particle_info(a_particle=a_particle)) then
                position = a_particle(4:6)
                density_array = calc_density_array(position)
                neutral_lattice_array = calc_new_lattice_with_density_info( &
                    density_array=density_array, &
                    lattice_array=neutral_lattice_array &
                )
            end if
        end do
        
        do pk = 1, size(ion_array(1, :))
            a_particle = ion_array(:, pk)
            if (has_particle_info(a_particle=a_particle)) then
                position = a_particle(4:6)
                density_array = calc_density_array(position)
                ion_lattice_array = calc_new_lattice_with_density_info( &
                    density_array=density_array, &
                    lattice_array=ion_lattice_array &
                )    
            end if
        end do

        do pk = 1, size(cex_array(1, :))
            a_particle = cex_array(:, pk)
            if (has_particle_info(a_particle=a_particle)) then
                position = a_particle(4:6)
                density_array = calc_density_array(position)
                cex_lattice_array = calc_new_lattice_with_density_info( &
                    density_array=density_array, &
                    lattice_array=cex_lattice_array &
                )    
            end if
        end do
    end subroutine

    subroutine delete_particle_out_of_calc_area()
        implicit none
        integer :: pk
        do pk = 1, ITERATE_NEUTRAL_NUM
            if (.not. is_in_calc_area(neutral_array(4:6, pk))) then
                neutral_array(:, pk) = 0
            end if
        enddo

        do pk = 1, ITERATE_ION_NUM
            if (.not. is_in_calc_area(ion_array(4:6, pk))) then
                ion_array(:, pk) = 0
            end if
        enddo
    end subroutine

    subroutine align_particle_array()
        implicit none
        integer :: pk1, pk2
        integer :: flag_pk
        do pk1 = 1, ITERATE_NEUTRAL_NUM
            if (.not. has_particle_info(a_particle=neutral_array(:, pk1))) then
                flag_pk = pk1
                do pk2 = flag_pk, ITERATE_NEUTRAL_NUM
                    if (has_particle_info(a_particle=neutral_array(:, pk2))) then
                        neutral_array(:, flag_pk) = neutral_array(:, pk2)
                        neutral_array(:, pk2) = 0
                        exit
                    end if
                enddo
            end if
        enddo

        do pk1 = 1, ITERATE_ION_NUM
            if (.not. has_particle_info(a_particle=ion_array(:, pk1))) then
                flag_pk = pk1
                do pk2 = flag_pk, ITERATE_ION_NUM
                    if (has_particle_info(a_particle=ion_array(:, pk2))) then
                        ion_array(:, flag_pk) = ion_array(:, pk2)
                        ion_array(:, pk2) = 0
                        exit
                    end if
                enddo
            end if
        enddo

        do pk1 = 1, size(cex_array(1, :))
            if (.not. has_particle_info(a_particle=cex_array(:, pk1))) then
                flag_pk = pk1
                do pk2 = flag_pk, size(cex_array(1, :))
                    if (has_particle_info(a_particle=cex_array(:, pk2))) then
                        cex_array(:, flag_pk) = cex_array(:, pk2)
                        cex_array(:, pk2) = 0
                        exit
                    end if
                enddo
            end if
        enddo


    end subroutine

end module iterate