/////////////////// 物理量 ///////////////////
// particle
float electron_charge = -1.602e-19;
float electron_mass = 9.10938356e-31;

// permittivity(誘電率)
float vaccum_permittivity = 8.8541878128e-12;


///////////////// 初期設定 /////////////////
// field
float potential_of_screengrid = 100;

// position
float position_of_screengrid = -10;
float position_of_accelgrid = 0;

// 微分の際に使う
float delta_x = 0.001;

// イオンのモデル
float charge = -1.602e-19 * 2;
float mass = 9.10938356e-31 * 2;
