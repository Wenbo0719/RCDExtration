import numpy as np
import matplotlib.pyplot as plt


def compute_polygon_area(points):
    point_num = len(points)
    if(point_num < 3): return 0.0
    s = points[0][1] * (points[point_num-1][0] - points[1][0])

    for i in range(1, point_num):
        s += points[i][1] * (points[i-1][0] - points[(i+1)%point_num][0])
    return abs(s/2.0)

if __name__ == '__main__':

    data1 = np.loadtxt("data/15up.txt", dtype=np.float32, delimiter=' ')
    polygon1 = data1[:, 0:2]
    data2 = np.loadtxt("data/15down.txt", dtype=np.float32, delimiter=' ')
    polygon2 = data2[:, 0:2]
    polygon = np.vstack((polygon1,polygon2))

    print(polygon1)
    print(polygon2)
    print(compute_polygon_area(polygon))

    plt.scatter(polygon[:, 0], polygon[:, 1])
    plt.show()