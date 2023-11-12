from matplotlib.figure import Figure
import numpy as np
import base64
from io import BytesIO
from sympy import diff, solve, symbols


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


def get_cubic_func_points(*coef):
    """Return list of coordinate of stationary and intersecting axis points of cubic function"""

    points = []

    x = symbols('x')

    # cubic function
    f_x = coef[0]*x**3 + coef[1]*x**2 + coef[2]*x + coef[3]

    # derivative of the cubic function
    f_prime = diff(f_x, x)

    # roots for identifying x-axis intersection
    x_roots = solve(f_prime, x)

    # find stationary points if the roots is float
    stationary_points = [[root, f_x.subs(x, root)]
                         for root in x_roots if type(root).__name__ == 'Float']
    stationary_points = [[round(float(coord[0]), 2), round(float(coord[1]), 2)]
                         for coord in stationary_points]

    # find y-axis intersection
    y_intercept = [0, round(float(f_x.subs(x, 0)), 2)]

    # find x-axis intersection
    x_intercept = [[round(root, 2), 0] for root in solve(f_x, x)]

    points = stationary_points + [y_intercept] + x_intercept

    return points


def draw_graph(func_type, *var):

    fig = Figure()
    ax = fig.subplots()

    if func_type == "linear":
        points = get_linear_func_points(var[0], var[1])

        xlim = get_coord_limit(get_highest_coord_value(points)[0])
        ylim = get_coord_limit(get_highest_coord_value(points)[1])

        # var for creating plot
        x = np.arange(*xlim, 0.01)
        y = var[0]*x + var[1]

    elif func_type == "quadratic":
        points = get_quadratic_func_points(var[0], var[1], var[2])

        xlim = get_coord_limit(get_highest_coord_value(points)[0])
        ylim = get_coord_limit(get_highest_coord_value(points)[1])

        # var for creating plot
        x = np.arange(*xlim, 0.01)
        y = var[0]*x**2 + var[1]*x + var[2]

    elif func_type == "cubic":
        points = get_cubic_func_points(*var)

        xlim = get_coord_limit(get_highest_coord_value(points)[0])
        ylim = get_coord_limit(get_highest_coord_value(points)[1])

        # var for creating plot
        x = np.arange(*xlim, 0.01)
        y = var[0]*x**3 + var[1]*x**2 + var[2]*x + var[3]

    ax.plot(x, y)

    # enable grid and limit the y-axis
    ax.grid(True)
    ax.set_ylim(*ylim)

    # draw x-axis and y-axis
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # draw extremum and intersecting points
    def get_point_marker_placement(x): return (
        x[0]+abs(x[0]*10/100), x[1]-abs(x[1]*10/100))

    for coord in points:
        try:
            ax.plot(coord[0], coord[1], marker="o", markersize=5,
                    markerfacecolor="red", markeredgecolor="black")
            ax.annotate(
                f"({str(round(coord[0], 2))}, {str(round(coord[1], 2))})", get_point_marker_placement(coord))
        except:
            pass

    buf = BytesIO()
    fig.savefig(buf, format="png")

    image = base64.b64encode(buf.getbuffer()).decode("ascii")
    func_exppr = get_func_exppr(*var)

    return (image, points, func_exppr)


def get_func_exppr(*numbers):
    func_exppr = ""

    for i, num in enumerate(numbers):
        num = int(num)
        exponent = len(numbers) - i - 1

        if num != 0:
            if num < 0:
                sign = "-"
            else:
                sign = "+"

            # Handling coefficient value
            if abs(num) != 1 and exponent > 1:
                func_exppr += f"{sign} {abs(num)}x<sup>{exponent}</sup>"
            elif abs(num) == 1 and exponent > 1:
                func_exppr += f" {sign} x<sup>{exponent}</sup>"
            elif abs(num) != 1 and exponent == 1:
                func_exppr += f" {sign} {abs(num)}x"
            elif abs(num) == 1 and exponent == 1:
                func_exppr += f" {sign} x"
            else:
                func_exppr += f" {sign} {abs(num)}"

    # Clean up if the func_exppr starts with a plus sign
    func_exppr = func_exppr.strip()

    if func_exppr.startswith("+ "):
        func_exppr = func_exppr[2:]

    return func_exppr


def get_highest_coord_value(coord_list):
    axis_limit = [0, 0]

    for coord in coord_list:
        x_coord = float(abs(coord[0]))
        y_coord = float(abs(coord[1]))

        if x_coord > axis_limit[0]:
            axis_limit[0] = x_coord

        if y_coord > axis_limit[1]:
            axis_limit[1] = y_coord

    return axis_limit


def get_coord_limit(x): return (-abs(x)*2, abs(x)*2)


# if __name__ == "__main__":
#     print(get_cubic_func_points(2, -3, 0, 0))
