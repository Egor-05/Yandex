import math


def solve(arr):
    if len(arr) == 3:
        a, b, c = arr
        D = (b ** 2) - (4 * a * c)
        if D > 0:
            print(' '.join([str((-b + math.sqrt(D)) / (2 * a)), str((-b - math.sqrt(D)) / (2 * a))]))
        elif D == 0:
            if (-b + math.sqrt(D)) / (2 * a) != -0.0:
                print((-b + math.sqrt(D)) / (2 * a))
            else:
                print(0.0)
        else:
            print('')
    elif len(arr) == 2:
        if arr[-1] / -arr[0] != -0.0:
            print(arr[-1] / -arr[0])
        else:
            print(0.0)
    else:
        if arr[-1] == 0:
            print('all')
        else:
            print('')


d = [int(i) for i in input().split()]
solve(d)
