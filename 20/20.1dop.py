import math


def roots_of_quadratic_equation(a, b, c):
    if a != 0 and b != 0:
        D = (b ** 2) - (4 * a * c)
        if D > 0:
            return [(-b + math.sqrt(D)) / (2 * a), (-b - math.sqrt(D)) / (2 * a)]
        elif D == 0:
            return [(-b + math.sqrt(D)) / (2 * a)]
    elif b == 0:
        return [math.sqrt(c), -math.sqrt(c)]
    elif a == 0:
        return [c]
    elif a == 0 and b == 0 and c == 0:
        return ['all']