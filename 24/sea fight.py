def inpt(*arr):
    arr = list(arr)
    print('\n'.join(goriz(arr)))
    print('\n'.join(vert(arr)))
    print('\n'.join(transp(arr)))
    print('\n'.join(goriz(transp(arr))))
    print('\n'.join(vert(transp(arr))))
    print('\n'.join(vert(goriz(transp(arr)))))


def goriz(matrix):
    for i in range(len(matrix)):
        matrix[i] = ''.join(list(reversed(matrix[i])))
    return matrix


def transp(mx):
    old = mx.copy()
    mx.clear()
    for i in range(len(old[0])):
        mx.append([0] * len(old))
    for i in range(len(old)):
        for j in range(len(old[i])):
            mx[j][i] = old[i][j]
    for i in range(len(mx)):
        mx[i] = ''.join(mx[i])
    return mx


def vert(matrix):
    matrix = list(reversed(matrix))
    for i in range(len(matrix)):
        matrix[i] = ''.join(list(reversed(matrix[i])))
    return matrix
