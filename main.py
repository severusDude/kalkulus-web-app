import matplotlib
import matplotlib.pyplot as plt
import numpy as np
matplotlib.use("Agg")


def draw_points(coefficient_a, coefficient_b, coefficient_c):
    points = []

    points.append([(-coefficient_b/(2*coefficient_a)), -(coefficient_b **
                  2-4*coefficient_a*coefficient_c)/(4*coefficient_a)])

    points.append([0, coefficient_c])

    points.extend([[x, 0] for x in np.roots(
        [coefficient_a, coefficient_b, coefficient_c])])

    return points
