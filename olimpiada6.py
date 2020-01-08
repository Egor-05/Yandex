a = int(input())
points = {}
for i in range(1, a + 1):
    points[i] = [int(j) for j in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
print(points)
print(b)
for j in b:
    x_p = j
    x_d = 0
    y_p = j
    y_d = 0
    for i in points:
        if x_d < abs(points[j][0] - points[i][0]) and points[i][1] == points[j][1]:
            x_d, x_p = abs(points[j][0] - points[i][0]), i
        if y_d < abs(points[j][1] - points[i][1]) and points[i][0] == points[j][0]:
            y_d, y_p = abs(points[j][1] - points[i][1]), i
    # if list(x.keys())[0] < 0:
    #     for e in x:
    #         x = {-e: x[e]}
    # if list(y.keys())[0] < 0:
    #     for e in y:
    #         y = {-e: y[e]}
    # if list(x.keys())[0] != list(y.keys())[0]:
    #     if list(x.keys())[0] > list(y.keys())[0]:
    #         if x[list(x.keys())[0]] >
    print(x_p, x_d, y_p, y_d)
