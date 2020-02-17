import math


def urav(a1, c1, a2, c2):
    b1 = b2 = 1
    x = (c1 * b2 - c2 * b1) / (b1 * a2 - b2 * a1)
    y = (c2 * a1 - c1 * a2) / (b1 * a2 - b2 * a1)
    return x, y


def equation(first_point, second_point, kb):
    first_pointx, first_pointy = [float(i) for i in first_point.split(";")]
    second_pointx, second_pointy = [float(i) for i in second_point.split(";")]
    a = 0
    if first_pointx - second_pointx != 0:
        a = (first_pointy - second_pointy) / (first_pointx - second_pointx)
    c = first_pointy - a * first_pointx
    if kb == 'a':
        return a
    elif kb == 'c':
        return c
    else:
        return [a, c]


b_x, b_y, c_x, c_y, d_x, d_y = [int(i) for i in input().split()]
u = 180 - (math.atan(equation('0;0', f'{b_x};{b_y}', 'k')) * 180 / math.pi
           + math.atan(equation(f'{c_x};{c_y}', f'{d_x};{d_y}', 'k') * 180 / math.pi))
k1, b1 = equation('0;0', f'{b_x};{b_y}', 'kb')
k2, b2 = equation(f'{c_x};{c_y}', f'{d_x};{d_y}', 'kb')
print(urav(k1, b1, k2, b2))
