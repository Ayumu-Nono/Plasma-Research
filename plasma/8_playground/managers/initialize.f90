module initialize
    use particle
    use lattice
contains
    subroutine init_all()
        call init_particles()
        call init_lattice()
    end subroutine
end module initialize