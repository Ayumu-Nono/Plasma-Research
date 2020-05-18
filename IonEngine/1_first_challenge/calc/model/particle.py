

class Particle:
    def set_charge(self, charge) -> None:
        self.charge = charge

    def set_mass(self, mass) -> None:
        self.mass = mass


def main():
    p = Particle()
    p.set_mass(p.electron_mass * 2)

    p.test1()


if __name__ == "__main__":
    main()
