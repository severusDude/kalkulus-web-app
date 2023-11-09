from matplotlib.figure import Figure
import numpy as np
import base64
from io import BytesIO


def get_linear_func_points(coef, const):
    """Return list of coordinate of intersecting axis points of linear function"""

    points = []

    points.append([0, const])
    points.append([-const/coef, 0])

    return points


def get_quadratic_func_points(*coef):
    """Return list of coordinate of extremum and intersecting axis points of quadratic function"""

    points = []

    points.append([(-coef[1]/(2*coef[0])), -(coef[1] **
                  2-4*coef[0]*coef[2])/(4*coef[0])])

    points.append([0, coef[2]])

    points.extend([[x, 0] for x in np.roots(
        [coef[0], coef[1], coef[2]])])

    return points


def draw_graph(func_type, *var):

    fig = Figure()
    ax = fig.subplots()

    if func_type == "linear":
        points = get_linear_func_points(var[0], var[1])

        # var for creating plot
        x = np.arange(
            *get_coord_limit(get_highest_coord_value(points)[0]), 0.01)
        y = (var[0]*x) + var[1]

    elif func_type == "quadratic":
        points = get_quadratic_func_points(var[0], var[1], var[2])

        # var for creating plot
        x = np.arange(
            *get_coord_limit(get_highest_coord_value(points)[0]), 0.01)
        y = (var[0]*x)**2 + (var[1]*x) + (var[2])

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

    ax.plot(x, y)

    # enable grid and limit the y-axis
    ax.grid(True)
    ax.set_ylim(*get_coord_limit(get_highest_coord_value(points)[1]))

    # draw x-axis and y-axis
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # draw extremum and intersecting points
    def get_point_marker_placement(x): return (
        x[0]+abs(x[0]*10/100), x[1]-abs(x[1]*10/100))

    for coord in points:
        ax.plot(coord[0], coord[1], marker="o", markersize=5,
                markerfacecolor="red", markeredgecolor="black")
        ax.annotate(
            f"({str(round(coord[0], 2))}, {str(round(coord[1], 2))})", get_point_marker_placement(coord))

    buf = BytesIO()
    fig.savefig(buf, format="png")

    image = base64.encode(buf.getbuffer()).decode("ascii")

    return image

# if __name__ == "__main__":
#     draw_graph(2, 2, -4)
