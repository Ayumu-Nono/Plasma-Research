import numpy as np
import mat

class SetPotential:
    def set_csv_path(self, path):
        self.csv_path = path

    def mk_csv_file(self, data):
        f = open(self.csv_path, 'w')
        f.write(data)
        f.close

    def set_potential(self, length):
        x = np.arange(length)/length
        y = 1 - (x-np.median(x))**2
        potential = y
        print(potential)

    def draw(self):
        



def main():
    p = SetPotential()
    p.set_csv_path("../dataset/potential.csv")
    p.mk_csv_file("でーた")
    p.set_potential(100)


if __name__ =='__main__':
    main()