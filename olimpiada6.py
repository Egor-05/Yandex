a = int(input())
points = {}
for i in range(1, a + 1):
    points[i] = [int(j) for j in input().split()]
b = [int(i) for i in input().split()]
c = [int(i) for i in input().split()]
for j in b:
    x_p = j
    x_d = 0
    y_p = j
    y_d = 0
    for i in points:
        if points[i][1] == points[j][1]:
            if abs(x_d) < abs(points[j][0] - points[i][0]):
                x_d, x_p = points[j][0] - points[i][0], i
            elif abs(x_d) == abs(points[j][0] - points[i][0]):
                if points[i][0] < points[x_p][0]:
                    x_d, x_p = points[j][0] - points[i][0], i
        if points[i][0] == points[j][0]:
            if abs(y_d) < abs(points[j][1] - points[i][1]):
                y_d, y_p = points[j][1] - points[i][1], i
            elif abs(y_d) == points[j][1] - points[i][1]:
                if points[i][1] < points[y_p][1]:
                    y_d, y_p = points[j][1] - points[i][1], i
    print(x_d, x_p)
    if x_d != y_d:
        if x_d > y_d:
            points[j][0] += (x_d * 2)
        else:
            points[j][1] += (y_d * 2)
    else:
        if points[x_p][0] > points[j][0]:
            points[j][0] += (x_d * 2)
        elif points[x_p][0] < points[j][0]:
            points[j][0] -= (x_d * 2)
a1 = abs(points[c[0]][0] - points[c[1]][0])
b1 = abs(points[c[0]][1] - points[c[1]][1])
if a1 != 0 and b1 != 0:
    print(a1 * b1)
else:
    print(0)
