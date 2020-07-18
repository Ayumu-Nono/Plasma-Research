import numpy as np
import pandas as pd


class Save:
    def __init__(self, outfile: str) -> None:
        self.outfile = outfile

    def add_row(self, array: np.array) -> None:
        f = open(self.outfile, "a")
        for axis in range(3):
            f.write(str(array[axis]) + ",")
        f.write("\n")
        f.close()

def main():
    save = Save('outdata.csv')


if __name__ == "__main__":
    main()