program evaluate
    use numerical_quantity
    use physical_quantity
    use array_debug
    use particle
    use lattice
    use initialize
    use iterate
    use output
    implicit none
    integer :: time_step
    integer :: progress
    call init_all()
    call receive_info_from_initializer()
    print *, "Start iterating"
    do time_step = 1, END_STEP
        ! print *, "Itereating...", time_step
        progress = int((real(time_step-1) / real(END_STEP)) * 100)
        call progressbar(progress, 0)
        call each_step()
    end do
    call save_particle_array_as_csv()

    contains
    subroutine progressbar(iparcent,uni)
        use iso_fortran_env
        implicit none
        integer,intent(in) :: iparcent
        integer,intent(in) :: uni
        integer :: i
        character(len=1),parameter :: esc=achar(27)
        character(len=1),parameter :: cr=achar(13)
        i=1
        write(uni,'(A)',advance='no') esc//"[1A"//esc//"[0J"
        write(uni,'(A)',advance='no') cr//"|"
        do while(i<iparcent/2)
            write(uni,'(A,I3)',advance='no') "="
            i=i+1
        end do
        select case(mod(i,3))
        case(0)
            write(uni,'(A,I3)',advance='no') "\"
        case(1)
            write(uni,'(A,I3)',advance='no') "/"
        case default
            write(uni,'(A,I3)',advance='no') "."
        end select
        do while(i<100/2)
            write(uni,'(A,I3)',advance='no') " "
            i=i+1
        end do
        write(uni,'(A,I3,A)',advance='yes') "|",iparcent,"%"
    end subroutine
end program evaluate