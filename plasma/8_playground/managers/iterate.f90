module iterate
    use numerical_quantity
    use particle
    use lattice
    use random_utils
    use calc_electric_field
    use density
    use charge_exchange
    use velocity_sum
    use motion
    use array_debug
    implicit none
    real, PUBLIC :: neutral_array(PARTICLE_MODEL_DIMENSION, ITERATE_NEUTRAL_NUM)
    real, PUBLIC :: ion_array(PARTICLE_MODEL_DIMENSION, ITERATE_ION_NUM)
    real, PUBLIC :: cex_array(PARTICLE_MODEL_DIMENSION, ITERATE_CEX_NUM)
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
        call update_particles_model()
        call generate_cex_ions()
        call add_new_particles()
    end subroutine

    subroutine add_new_particles()
        implicit none
        
    end subroutine
    

    subroutine generate_cex_ions()
        implicit none
        real :: generate_rate_on_grid, generate_num
        integer :: x, y, z
        integer :: pk
        
        do z = 1, LATTICE_NUM
            do y = 1, LATTICE_NUM
                do x = 1, LATTICE_NUM
                    generate_rate_on_grid = calc_generate_rate_on_grid( &
                        neutral_density=neutral_lattice_array(1, x, y, z), &
                        ion_density=ion_lattice_array(1, x, y, z), &
                        neutral_velocity=calc_average_velocity(neutral_lattice_array(:, x, y, z)), &
                        ion_velocity=calc_average_velocity(ion_lattice_array(:, x, y, z)) &                   
                    )
                    generate_num = round_with_bias(generate_rate_on_grid)
                    generate_num = int(generate_num)
                    call generate_cex(position=real((/x, y, x/)), generate_num=generate_num)
                end do
            end do
        end do

    end subroutine

    subroutine generate_cex(position, generate_num)
        implicit none
        real, intent(in) :: position(3)
        real, intent(in) :: generate_num
        integer :: pk
        real :: counter
        logical :: is_generate_success = .false.
        counter = generate_num
        do while (counter > 0)
            counter = counter - 1
            do pk = 1, ITERATE_CEX_NUM
                if (.not. has_particle_info(cex_array(:, pk))) then
                    cex_array(:, pk) = return_initial_cex_particle(position=position)
                    is_generate_success = .true.
                end if
            end do
            if (.not. is_generate_success) then
                print *, "ERROR: in iterate module"
                print *, "shortage of cex_array length."
                STOP
            end if
        end do
    end subroutine

    subroutine update_particles_model()
    implicit none
    integer :: pk
    real :: a_particle(PARTICLE_MODEL_DIMENSION)
    real :: position(3)
    do pk = 1, size(neutral_array(1, :))
        a_particle = neutral_array(:, pk)
        position = a_particle(4:6)
        if (has_particle_info(a_particle=a_particle)) then
            a_particle = calc_new_particle_model( &
                particle=a_particle, &
                magnetic_field=(/0.0, 0.0, 0.0/), &
                electric_field=calc_electric_field_on_free_point(position) &
            )
            neutral_array(:, pk) = a_particle
        end if
    end do

    do pk = 1, size(ion_array(1, :))
        a_particle = ion_array(:, pk)
        position = a_particle(4:6)
        if (has_particle_info(a_particle=a_particle)) then
            a_particle = calc_new_particle_model( &
                particle=a_particle, &
                magnetic_field=(/0.0, 0.0, 0.0/), &
                electric_field=calc_electric_field_on_free_point(position) &
            )
            ion_array(:, pk) = a_particle
        end if
    end do

    do pk = 1, size(cex_array(1, :))
        a_particle = cex_array(:, pk)
        position = a_particle(4:6)
        if (has_particle_info(a_particle=a_particle)) then
            a_particle = calc_new_particle_model( &
                particle=a_particle, &
                magnetic_field=(/0.0, 0.0, 0.0/), &
                electric_field=calc_electric_field_on_free_point(position) &
            )
            cex_array(:, pk) = a_particle
        end if
    end do
    end subroutine update_particles_model

    subroutine calc_field()
        call calc_electric_potential_with_no_collision(ion_density=ion_lattice_array(1, :, :, :))
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
        real :: a_particle(PARTICLE_MODEL_DIMENSION)
        do pk = 1, size(neutral_array(1, :))
            a_particle = neutral_array(:, pk)
            if (has_particle_info(a_particle=a_particle)) then
                neutral_lattice_array = calc_new_lattice_with_density_info( &
                    density_array=calc_density_array(a_particle), &
                    lattice_array=neutral_lattice_array &
                )
                neutral_lattice_array = calc_new_lattice_with_velocity_sum_info( &
                    velocity_sum_array=calc_velocity_sum_array(a_particle), &
                    lattice_array=neutral_lattice_array &
                )
            end if
        end do
        
        do pk = 1, size(ion_array(1, :))
            a_particle = ion_array(:, pk)
            if (has_particle_info(a_particle=a_particle)) then
                ion_lattice_array = calc_new_lattice_with_density_info( &
                    density_array=calc_density_array(a_particle), &
                    lattice_array=ion_lattice_array &
                )
                ion_lattice_array = calc_new_lattice_with_velocity_sum_info( &
                    velocity_sum_array=calc_velocity_sum_array(a_particle), &
                    lattice_array=ion_lattice_array &
                )
            end if
        end do

        do pk = 1, size(cex_array(1, :))
            a_particle = cex_array(:, pk)
            if (has_particle_info(a_particle=a_particle)) then
                cex_lattice_array = calc_new_lattice_with_density_info( &
                    density_array=calc_density_array(a_particle), &
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