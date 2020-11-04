from matplotlib import pyplot as plt
import numpy as np
import math


def produce_fragment(x, y):
    x = abs(x)
    y = abs(y)
    return math.floor(x) + 0.5, math.floor(y) + 0.5


def raster_rect(x1, y1, x2, y2):
    x = x1
    y = y1

    x_axis = []
    y_axis = []

    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    m = delta_y / delta_x
    b = y - m * x

    pixel_x, pixel_y = produce_fragment(x, y)
    x_axis.append(pixel_x)
    y_axis.append(pixel_y)

    while x < x2:
        x += 1
        y = m * x + b
        pixel_x, pixel_y = produce_fragment(x, y)
        x_axis.append(pixel_x)
        y_axis.append(pixel_y)
    return {'x': x_axis, 'y': y_axis}


def plot_chart(x_axis, y_axis):
    plt.scatter(x_axis, y_axis)
    plt.grid()
    plt.yticks(range(0, math.ceil(y_axis[-1]) + 1))
    plt.xticks(range(0, math.ceil(x_axis[-1]) + 1))
    plt.show()


x_size = 12
axis = raster_rect(0, 1, 5, 3)
plot_chart(axis['x'], axis['y'])
print(axis)
