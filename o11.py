import math


def urav(k, b):
    x = (2 * b) / (-2 * k)


def equation(first_point, second_point, kb):
    first_pointx, first_pointy = [float(i) for i in first_point.split(";")]
    second_pointx, second_pointy = [float(i) for i in second_point.split(";")]
    k = 0
    if first_pointx - second_pointx != 0:
        k = (first_pointy - second_pointy) / (first_pointx - second_pointx)
    b = first_pointy - k * first_pointx
    if kb == 'k':
        return k
    elif kb == 'b':
        return b
    else:
        return [k, b]


def equation1(x1, y1, x2, y2):



b_x, b_y, c_x, c_y, d_x, d_y = [int(i) for i in input().split()]
u = 180 - (math.atan(equation('0;0', f'{b_x};{b_y}', 'k')) * 180 / math.pi
           + math.atan(equation(f'{c_x};{c_y}', f'{d_x};{d_y}', 'k') * 180 / math.pi))
k1, b1 = equation('0;0', f'{b_x};{b_y}', 'kb')
k2, b2 = equation(f'{c_x};{c_y}', f'{d_x};{d_y}', 'kb')
print(urav(k1, b1))
