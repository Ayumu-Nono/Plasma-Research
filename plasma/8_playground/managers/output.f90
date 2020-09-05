module output
    use numerical_quantity
    use particle
    use iterate
    implicit none
    
contains
    subroutine save_particle_array_as_csv()
        implicit none
        integer :: pk
        open (1000, file='../outdata/neutrals.csv', status='replace')
        do pk = 1, size(neutral_array(1, :))
            write (1000, *) neutral_array(:, pk)
        end do
        close (1000)
    end subroutine
end module output