from matplotlib import pyplot as plt
import numpy as np
import math


def produce_fragment(x, y):
    x = abs(x)
    y = abs(y)
    return math.floor(x), math.floor(y)


def raster_to_x(x1, y1, x2, y2, m):
    x_axis = []
    y_axis = []

    x = x1
    y = y1

    b = y - m * x

    step = 1 if x2 > x1 else -1

    mat = np.zeros((int(abs(y1 - y2)) + 1, int(abs(x1 - x2)) + 1))

    pixel_x, pixel_y = produce_fragment(x, y)
    x_axis.append(pixel_x)
    y_axis.append(pixel_y)

    mat[int(pixel_y)][int(pixel_x)] = 5

    while x != x2:
        x += step
        y = m * x + b
        mat[int(y)][int(x)] = 5
        pixel_x, pixel_y = produce_fragment(x, y)
        x_axis.append(pixel_x)
        y_axis.append(pixel_y)
    return {'x': x_axis, 'y': y_axis, 'm': mat}


def raster_to_y(x1, y1, x2, y2, m):
    x_axis = []
    y_axis = []

    x = x1
    y = y1

    b = y - m * x

    step = 1 if y2 > y1 else -1

    mat = np.zeros((int(abs(y1 - y2)) + 1, int(abs(x1 - x2)) + 1))

    pixel_x, pixel_y = produce_fragment(x, y)
    x_axis.append(pixel_x)
    y_axis.append(pixel_y)

    mat[int(pixel_y)][int(pixel_x)] = 5

    while y != y2:
        y += step
        x = x if m == 0 else (y - b) / m
        mat[int(y)][int(x)] = 5
        pixel_x, pixel_y = produce_fragment(x, y)
        x_axis.append(pixel_x)
        y_axis.append(pixel_y)
    return {'x': x_axis, 'y': y_axis, 'm': mat}


def raster_rect(x1, y1, x2, y2, size_x, size_y):
    size_x -= 1
    size_y -= 1

    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    x_scale = 1 if delta_x == 0 else size_x / delta_x
    y_scale = 1 if delta_y == 0 else size_y / delta_y

    x1 *= x_scale
    x2 *= x_scale

    y1 *= y_scale
    y2 *= y_scale

    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    m = 0 if delta_x == 0 else delta_y / delta_x

    return raster_to_x(x1, y1, x2, y2, m) if delta_x >= delta_y else raster_to_y(x1, y1, x2, y2, m)


def plot_chart(x_axis, y_axis, mat):
    height = range(math.floor(min(y_axis[-1], y_axis[0])), math.ceil(max(y_axis[-1], y_axis[0])) + 1)
    width = range(math.floor(min(x_axis[-1], x_axis[0])), math.ceil(max(x_axis[-1], x_axis[0])) + 1)

    plt.matshow(mat)
    plt.yticks(height)
    plt.xticks(width)
    plt.show()


if __name__ == '__main__':
    x_size = 100
    y_size = 100
    axis = raster_rect(0, 0, 10, 10, x_size, y_size)
    plot_chart(axis['x'], axis['y'], axis['m'])
