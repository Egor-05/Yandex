<<<<<<< HEAD
for i in range(1, 19, 2):
        print(i)
=======
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


print(roots_of_quadratic_equation(3, -25, 8))
>>>>>>> 11899a3a4ee2933fa1f2436947f6ff5a2580bce0
