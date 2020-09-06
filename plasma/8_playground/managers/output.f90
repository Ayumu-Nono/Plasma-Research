module output
    use numerical_quantity
    use particle
    use iterate
    implicit none
    
contains
    subroutine save_particle_array_as_csv()
        implicit none
        integer :: pk
        character :: linebuf*256
        open (1000, file='../outdata/neutrals.csv', status='replace')
        write (linebuf, *) "position_x,","position_y,","position_z" ! 一旦内部ファイルへ書き出す
        call del_spaces(linebuf)           ! 余分な空白を削除する
        write (1000, '(a)') trim(linebuf)    ! 出力する
        do pk = 1, size(neutral_array(1, :))
            if (has_particle_info(neutral_array(:, pk))) then
                write (1000, *) neutral_array(4, pk),",",neutral_array(5, pk),",",neutral_array(6, pk)
            end if
        end do
        close (1000)
    end subroutine

    subroutine del_spaces(s)
        character (*), intent (inout) :: s
        character (len=len(s)) tmp
        integer i, j
        j = 1
        do i = 1, len(s)
            if (s(i:i)==' ') cycle
            tmp(j:j) = s(i:i)
            j = j + 1
        end do
        s = tmp(1:j-1)
    end subroutine del_spaces
end module output