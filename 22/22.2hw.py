def transpose(mx):
    matrix = mx.copy()
    print(id(mx))
    mx.clear()
    for i in range(len(matrix[0])):
        mx.append([0] * len(matrix))
    print(id(mx))
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            mx[j][i] = matrix[i][j]
