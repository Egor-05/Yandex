import numpy as np
from itertools import combinations


def is_not_under_attack(y1, x1, arr):
    for y2, x2 in arr:
        if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
            return False
    return True


def queens(size):
    b = [i for i in range(size)]
    c = b.copy()
    for i in range(size - 1):
        b += c
    lst = set()
    for i in combinations(b, size):
        if len(i) == len(set(i)):
            points = [(j, int(i[j])) for j in range(len(i))]
            n = True
            for j in points:
                if not is_not_under_attack(j[0], j[1], [e for e in points if e != j]):
                    n = False
                    break
            if n:
                lst.add(''.join([str(int(j) + 1) for j in i]))
    for i in sorted(list(lst)):
        print(i)


queens(6)