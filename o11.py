import math


def line_intersection(line1, line2):
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


def equation(first_point, second_point, kb):
    first_pointx, first_pointy = [float(i) for i in first_point.split(";")]
    second_pointx, second_pointy = [float(i) for i in second_point.split(";")]
    a = 0
    if first_pointx - second_pointx != 0:
        a = (first_pointy - second_pointy) / (first_pointx - second_pointx)
    c = first_pointy - a * first_pointx
    if kb == 'k':
        return a
    elif kb == 'b':
        return c
    else:
        return [a, c]


b_x, b_y, c_x, c_y, d_x, d_y = [int(i) for i in input().split()]
u = 180 - (math.atan(equation('0;0', f'{b_x};{b_y}', 'k')) * 180 / math.pi
           + math.atan(equation(f'{c_x};{c_y}', f'{d_x};{d_y}', 'k')) * 180 / math.pi)
print(line_intersection(([0, 0], [b_x, b_y]), ([c_x, c_y], [d_x, d_y])), u)
u1 = 180 - u - math.atan(equation(f'{c_x};{c_y}', f'{d_x};{d_y}', 'k')) * 180 / math.pi

