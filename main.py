from matplotlib import pyplot as plt
import numpy as np
import math


def produce_fragment(x, y):
    """
    Função responsável por converter uma coordenada em uma amostra discreta.

    :param x: x do vértice
    :param y: y do vértice
    :return: ccoordenada do fragmento em forma de tupla
    """
    x = abs(x)
    y = abs(y)
    return math.floor(x), math.floor(y)


def raster_to_x(x1, y1, x2, y2, m):
    """
    Função responsável por rasterizar uma reta a partir de seus vértices, quando
    a variação em x é maior do que em y.

    :param x1: x do vértice 1
    :param y1: y do vértice 1
    :param x2: x do vértice 2
    :param y2: y do vértice 2
    :param m: Coeficiente angular da reta
    :return: Objeto contendo as listas de valores de x e y das amostras discretas e uma
            matriz com os pixels mapeados.
    """
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
    """
    Função responsável por rasterizar uma reta a partir de seus vértices, quando
    a variação em x é maior do que em y.

    :param x1: x do vértice 1
    :param y1: y do vértice 1
    :param x2: x do vértice 2
    :param y2: y do vértice 2
    :param m: Coeficiente angular da reta
    :return: Objeto contendo as listas de valores de x e y das amostras discretas e uma
            matriz com os pixels mapeados.
    """
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


def raster_rect(x1: float, y1: float, x2: float, y2: float, size_x: int, size_y: int):
    """
    Função responsável por receber dois vértices de uma reta e escolher a melhor
    estratégia para rasterizá-la.

    :param x1: x do vértice 1
    :param y1: y do vértice 1
    :param x2: x do vértice 2
    :param y2: y do vértice 2
    :param size_x: Quantidade de pixels no eixo x
    :param size_y: Quantidade de pixels no eixo y
    :return: Objeto contendo as listas de valores de x e y das amostras discretas e uma
            matriz com os pixels mapeados.
    """
    size_x -= 1
    size_y -= 1

    delta_x: float = abs(x2 - x1)
    delta_y: float = abs(y2 - y1)

    x_scale: int = 1 if delta_x == 0 else size_x / delta_x
    y_scale: int = 1 if delta_y == 0 else size_y / delta_y

    x1 *= x_scale
    x2 *= x_scale

    y1 *= y_scale
    y2 *= y_scale

    delta_x = abs(x2 - x1)
    delta_y = abs(y2 - y1)

    m: float = 0 if delta_x == 0 else delta_y / delta_x

    return raster_to_x(x1, y1, x2, y2, m) if delta_x >= delta_y else raster_to_y(x1, y1, x2, y2, m)


def plot_chart(x_axis, y_axis, mat):
    """
    Função responsável por gerar uma imagem de uma reta rasterizada a partir dos dados
    obtidos no algoritmo de rasterização.
    :param x_axis: Lista de valores de x das amostras discretas
    :param y_axis: Lista de valores de x das amostras discretas
    :param mat: Matriz de pixels da reta discretizada
    :return:
    """
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
