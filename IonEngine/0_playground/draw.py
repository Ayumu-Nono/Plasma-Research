import csv
import matplotlib.pyplot as plt

# from mpl_toolkits.mplot3d import Axes3D


class Draw(object):
    def drawGraph(self):
        time = []
        position_x = []
        position_y = []

        csv_file = open('output.csv', 'r')

        for row in csv.reader(csv_file):
            # print(row)
            time.append(float(row[0]))
            position_x.append(float(row[1]))
            position_y.append(float(row[2]))

        t = time
        x = position_x
        y = position_y

        for i in range(len(t)):
            plt.scatter(x[i], y[i])
            # plt.show()
            path = 'figure/output_' + str(i) + 'in' + str(len(t) - 1) + '.png'
            plt.savefig(path)
