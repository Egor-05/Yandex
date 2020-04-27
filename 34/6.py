import numpy as np


def points(line, numpoint):
    if numpoint + 1 < len(line) and numpoint - 1 >= 0:
        a1 = line[numpoint - 1]
        a3 = line[numpoint + 1]
    elif numpoint + 1 < len(line) and numpoint - 1 < 0:
        a1 = line[-1]
        a3 = line[numpoint + 1]
    elif numpoint + 1 >= len(line) and numpoint - 1 >= 0:
        a1 = line[numpoint - 1]
        a3 = line[0]
    else:
        a1 = line[-1]
        a3 = line[0]
    return a1, a3


def generation(line):
    a = np.array([[int(i) for i in line]])
    b = np.zeros(10 * len(line)).reshape(10, len(line))
    a = np.concatenate((a, b))
    for i in range(1, 11):
        for j in range(len(line)):
            pp, ap = points(a[i - 1], j)
            if a[i - 1][j]:
                if not pp and ap:
                    a[i][j] = 1
                elif not pp and not ap:
                    a[i][j] = 1
                else:
                    a[i][j] = 0
            else:
                if pp and not ap:
                    a[i][j] = 1
                elif not pp and ap:
                    a[i][j] = 1
                else:
                    a[i][j] = 0
    return ''.join([str(int(i)) for i in a[10]])


print(generation("0100011001010110111000111100010100111111001011000011010000100000100010100101100001111011110110100001"))