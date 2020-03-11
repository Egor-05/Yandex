def inpt(*arr):
    arr = list(arr)
    print('\n'.join(goriz(arr)))
    print('\n'.join(vert(arr)))
    print('\n'.join(transp(arr)))
    print('\n'.join(goriz(transp(arr))))
    print('\n'.join(vert(transp(arr))))
    print('\n'.join(vert(goriz(transp(arr)))))


def goriz(matrix):
    m = matrix.copy()
    for i in range(len(m)):
        m[i] = ''.join(list(reversed(m[i])))
    return m


def transp(mx):
    old = mx.copy()
    mx1 = []
    for i in range(len(old[0])):
        mx1.append([0] * len(old))
    for i in range(len(old)):
        for j in range(len(old[i])):
            mx1[j][i] = old[i][j]
    for i in range(len(mx1)):
        mx1[i] = ''.join(mx1[i])
    return mx1


def vert(matrix):
    matrix1 = list(reversed(matrix))
    for i in range(len(matrix1)):
        matrix1[i] = ''.join(list(reversed(matrix1[i])))
    return matrix1
