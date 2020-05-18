import numpy as np

from .pysical_quantity import PysicalQuantity
from .particle import Particle
from .initial_condition import InitialCondition


class Field(PysicalQuantity, Particle, InitialCondition):
    # ポテンシャルを微分して電場を算出
    def electron_field(self) -> np.array:
        divide = self.position_of_screengrid / self.delta_x  # 分割数
        x = -self.position_of_screengrid + np.arange(divide) * self.delta_x
        x = x / self.position_of_screengrid
        phi = self.set_potential_x()
        x_delta_plus = x + self.delta_x
        phi_delta_plus = self.set_potential_x()
        d_phi = phi_delta_plus - phi
        electron_field = d_phi
        print(x)
        return electron_field

    # 位置xでのポテンシャルを定義(x<0)
    def set_potential_x(self) -> np.array:
        divide = self.position_of_screengrid / self.delta_x  # 分割数
        x = -self.position_of_screengrid + np.arange(divide) * self.delta_x
        self.x = x
        phi = 1 - (x / self.position_of_screengrid + 1) ** (4 / 3)
        phi = phi * self.potential_of_screengrid
        phi = phi / self.position_of_screengrid
        self.potential = phi

    # 最大限界電流密度(スクリーングリッドの位置とポテンシャルで決まる)
    def calc_current_density(self) -> float:
        databox = (4 / 9) * self.vaccum_permittivity
        databox = databox * (self.charge / self.mass) ** (1 / 2)
        databox = databox * self.potential_of_screengrid ** (3 / 2)
        databox = databox * self.position_of_screengrid ** (-2)
        return databox

    # 簡略化のために作った関数。グザイを算出する。
    def calc_guzai(self):
        j = self.calc_current_density()
        epsilon_0 = self.vaccum_permittivity
        guzai = j / (epsilon_0 * (self.charge / self.mass) ** (1 / 2))
        return guzai


def main():
    field = Field()
    field.set_charge(-1.602 * 10 ** -19)
    field.set_mass(9.10938356 * 10 ** -31)
    field.set_1d_electron_field()


if __name__ == "__main__":
    main()
