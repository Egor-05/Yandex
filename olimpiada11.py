import math


def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return ['all']
    elif a != 0 and b != 0:
        D = (b ** 2) - (4 * a * c)
        if D > 0:
            return [(-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)]
        elif D == 0:
            return [(-b + math.sqrt(D)) / (2 * a)]
        else:
            return []
    elif b == 0 and a != 0:
        return [math.sqrt(c / a), -math.sqrt(c / a)]
    elif a == 0 and b != 0:
        return [c / -b]
    else:
        return []


def intersection(center, radius, p1, p2):
    dx, dy = p2[0] - p1[0], p2[1] - p1[1]
    a = dx**2 + dy**2
    b = 2 * (dx * (p1[0] - center[0]) + dy * (p1[1] - center[1]))
    c = (p1[0] - center[0])**2 + (p1[1] - center[1])**2 - radius**2
    discriminant = b**2 - 4 * a * c
    t1 = (-b + discriminant**0.5) / (2 * a)
    t2 = (-b - discriminant**0.5) / (2 * a)
    return [dx * t1 + p1[0], dy * t1 + p1[1]], [dx * t2 + p1[0], dy * t2 + p1[1]]


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


def find_k(first_point, second_point, kb):
    first_pointx, first_pointy = [float(i) for i in first_point.split(";")]
    second_pointx, second_pointy = [float(i) for i in second_point.split(";")]
    k = 0
    if first_pointx - second_pointx != 0:
        k = (first_pointy - second_pointy) / (first_pointx - second_pointx)
    return k


b_x, b_y, c_x, c_y, d_x, d_y = [int(i) for i in input().split()]
delta = math.atan2(d_y - c_y, d_x - c_x) * 180 / math.pi
u = 180 - (math.atan2(b_y, b_x) * 180 / math.pi + (180 - delta))
x, y = line_intersection(([0, 0], [b_x, b_y]), ([c_x, c_y], [d_x, d_y]))
k = math.tan(180 - u - delta)
b = y - k * x
distance = math.hypot(b_x, b_y)
A = math.tan(180 - u - delta)
B = math.tan(90 - u - delta)
C = -A * x - B * y
print(A, B, C)
print(f'{y} = {k} * {x} + {b}, distance = {distance}, {u}, {delta}')
x1, x2 = intersection((0, 0), distance, (x, y), (3, k * 3 + b))
print(x1, x2)
