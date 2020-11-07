from matplotlib import pyplot as plt
import math


def produce_fragment(x, y):
    x = abs(x)
    y = abs(y)
    return math.floor(x) + 0.5, math.floor(y) + 0.5


def raster_to_x(x1, y1, x2, m):
    x_axis = []
    y_axis = []

    x = x1
    y = y1

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


def raster_to_y(x1, y1, y2, m):
    x_axis = []
    y_axis = []

    x = x1
    y = y1

    b = y - m * x

    pixel_x, pixel_y = produce_fragment(x, y)
    x_axis.append(pixel_x)
    y_axis.append(pixel_y)

    while y < y2:
        y += 1
        x = (y - b) / m
        pixel_x, pixel_y = produce_fragment(x, y)
        x_axis.append(pixel_x)
        y_axis.append(pixel_y)
    return {'x': x_axis, 'y': y_axis}


def raster_rect(x1, y1, x2, y2, size_x, size_y):
    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    x_scale = size_x / delta_x
    y_scale = size_y / delta_y

    x1 *= x_scale
    x2 *= x_scale

    y1 *= y_scale
    y2 *= y_scale

    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    m = delta_y / delta_x

    return raster_to_x(x1, y1, x2, m) if delta_x >= delta_y else raster_to_y(x1, y1, y2, m)


def plot_chart(x_axis, y_axis):
    height = range(math.floor(min(y_axis[-1], y_axis[0])), math.ceil(max(y_axis[-1], y_axis[0])) + 1)
    width = range(math.floor(min(x_axis[-1], x_axis[0])), math.ceil(max(x_axis[-1], x_axis[0])) + 1)

    plt.scatter(x_axis, y_axis)
    plt.grid()
    plt.yticks(height)
    plt.xticks(width)
    plt.show()


if __name__ == '__main__':
    x_size = 5
    y_size = 9
    axis = raster_rect(5, 0, 10, 20, x_size, y_size)
    plot_chart(axis['x'], axis['y'])
    print(axis)
