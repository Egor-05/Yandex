import numpy as np


def queens(size):
    lst = np.array([[]])
    for row in range(size):
        lst = add_queen(row, size, lst)
    for i in lst:
        print(''.join(str(j + 1).replace('.', '').replace('0', '') for j in i))


def add_queen(row, cols, lst):
    return [np.append(i, [j]) for i in lst for j in range(cols) if not_is_under_attack(row, j, i)]


def not_is_under_attack(row, col, lst):
    a = [lst[i] != col and lst[i] + i != col + row and lst[i] - i != col - row for i in range(row)]
    return all(a)


queens(4)