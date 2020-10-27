program fmt_output
    implicit none
    integer :: i = 1234
    real :: a = 1.234
    double precision :: d = 9.87654321d0
    complex :: c = (1.5,2.345)
    character(len=4) :: s = "abcd"
    print '(i10)', i         ! 幅 10、右寄せ
    print '(i0)', i          ! 左寄せ
    print '(1x,i0)', i       ! 1 文字空けて左寄せ
    print '(i1)', i          ! 幅が足りない場合はアスタリスクが出力される
    print '("x = ", f5.2)', 99999.0  ! 幅が足りない場合のもう１つの例
    write (*,'(i10.7)') i    ! 幅 10、右寄せ、最低出力桁数 7 (満たない場合は 0 を出力）
    print '(f10.2)', a       ! 幅 10、右寄せ、小数点以下 2 桁
    print '(f0.2)', a        ! 左寄せ、小数点以下 2 桁
    write (*,'(e10.3, f15.5)') a, d   ! 複数の書式指定をカンマで区切る例
    write (*,'(e10.3e1)') a           ! 指数部の桁数まで指定する例
    write (*,'(e10.4, f10.4)') c      ! 複素数は２つの実数の書式を指定する
    write (*,'(2f10.4)') c            ! 複素数を反復数 2 で指定する
    print '("(real=",f0.2," imag=",f0.2,")")', c ! 文字定数表現を書式指定に含める例
    print '(a)', s           ! 幅を指定しないと、宣言時の長さ（ここでは 4）が使われる例
    print '(a2)', s          ! 幅が足りない場合は切り捨てられる
    open(17, file='output.dat', status='replace')
    write (17,*) i
    close(17)
end program fmt_output