import numpy as np


def generation(line):
    a = [[int(i) for i in line]]
    for i in range(9):
        a.append([0] * len(a[0]))
    for i in range(1, 10):
        for j in range(len(a[i])):
            if not a[i - 1][j]:
                if j - 1 > -1 and j + 1 < len(a[i]):
                    if a[i - 1][j - 1] and not a[i - 1][j + 1]:
                        a[i][j] = 1
                    elif not a[i - 1][j - 1] and a[i - 1][j + 1]:
                        a[i][j] = 1
                elif j - 1 < 0 and j + 1 < len(a[i]):
                    if a[i - 1][-1] and not a[i - 1][j + 1]:
                        a[i][j] = 1
                    elif not a[i - 1][-1] and a[i - 1][j + 1]:
                        a[i][j] = 1
                else:
                    if a[i - 1][j - 1] and not a[i - 1][0]:
                        a[i][j] = 1
                    elif not a[i - 1][j - 1] and a[i - 1][0]:
                        a[i][j] = 1
            else:
                if j - 1 > -1 and j + 1 < len(a[i]):
                    if not a[i - 1][j - 1] and a[i - 1][j + 1]:
                        a[i][j] = 1
                    elif not a[i - 1][j - 1] and not a[i - 1][j + 1]:
                        a[i][j] = 1
                elif j - 1 > -1 and j + 1 < len(a[i]):
                    if not a[i - 1][-1] and a[i - 1][j + 1]:
                        a[i][j] = 1
                    elif not a[i - 1][-1] and not a[i - 1][j + 1]:
                        a[i][j] = 1
                else:
                    if not a[i - 1][j - 1] and a[i - 1][0]:
                        a[i][j] = 1
                    elif not a[i - 1][j - 1] and not a[i - 1][0]:
                        a[i][j] = 1

    return a[9]


