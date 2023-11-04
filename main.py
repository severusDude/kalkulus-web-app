import matplotlib
import matplotlib.pyplot as plt
import numpy as np
# matplotlib.use("Agg")


def draw_points(coefficient_a, coefficient_b, coefficient_c):
    points = []

    points.append([(-coefficient_b/(2*coefficient_a)), -(coefficient_b **
                  2-4*coefficient_a*coefficient_c)/(4*coefficient_a)])

    points.append([0, coefficient_c])

    points.extend([[x, 0] for x in np.roots(
        [coefficient_a, coefficient_b, coefficient_c])])

    return points


def draw_graph(coefficient_a, coefficient_b, coefficient_c):

    # get extremum and intersecting axis points
    points = draw_points(coefficient_a, coefficient_b, coefficient_c)
    print(points)

    def get_highest_coord_value(coord_list):
        axis_limit = [0, 0]

        for coord in coord_list:
            x_coord = abs(coord[0])
            y_coord = abs(coord[1])

            if x_coord > axis_limit[0]:
                axis_limit[0] = x_coord

            if y_coord > axis_limit[1]:
                axis_limit[1] = y_coord

        return axis_limit

    def get_coord_limit(x): return (-abs(x)*2, abs(x)*2)

    # var for creating plot
    x = np.arange(*get_coord_limit(get_highest_coord_value(points)[0]), 0.01)
    y = (coefficient_a*x)**2 + (coefficient_b*x) + (coefficient_c)

    plt.plot(x, y)

    # enable grid and limit the y-axis
    plt.grid(True)
    plt.ylim(*get_coord_limit(get_highest_coord_value(points)[1]))

    # draw x-axis and y-axis
    ax = plt.gca()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # draw extremum and intersecting points
    def get_point_marker_placement(x): return (
        x[0]+abs(x[0]*10/100), x[1]-abs(x[1]*10/100))

    for coord in points:
        plt.plot(coord[0], coord[1], marker="o", markersize=5,
                 markerfacecolor="red", markeredgecolor="black")
        plt.annotate(
            f"({str(round(coord[0], 2))}, {str(round(coord[1], 2))})", get_point_marker_placement(coord))

    plt.show()
    # plt.savefig("static/plot.png")


# if __name__ == "__main__":
#     draw_graph(2, 2, -4)
