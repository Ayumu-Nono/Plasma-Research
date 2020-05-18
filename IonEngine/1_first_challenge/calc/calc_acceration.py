from model.field import Field
import numpy as np


class CalcAcceration(Field):
    def calc_force(self, electron_field):
        force = electron_field * self.charge
        return force


def main():
    calc_accel = CalcAcceration()
    calc_accel.set_charge(-1.602 * 10 ** -19)
    calc_accel.set_mass(9.10938356 * 10 ** -31)
    field = calc_accel.electron_field()
    print(calc_accel.calc_force(field))


if __name__ == "__main__":
    main()
