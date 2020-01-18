points = [[int(i) for i in input().split()] for i in range(int(input()))]
b = [int(i) for i in input().split()]
c1, c2 = [int(i) for i in input().split()]
prev_p = -1
sx, sy = 0, 0
xdc, ydc = [], []
for j in b:
    pj = points[j - 1]
    if j == prev_p and sx != 0:
        xdc = [i - sx for i in xdc]
        ydc = [i[1] - pj[1] for i in points if i[0] == pj[0] and i[1] - pj[1] != 0]
    elif j == prev_p and sy != 0:
        xdc = [i[0] - pj[0] for i in points if i[1] == pj[1] and i[0] - pj[0] != 0]
        ydc = [i - sy for i in ydc]
    else:
        xdc = [i[0] - pj[0] for i in points if i[1] == pj[1] and i[0] - pj[0] != 0]
        ydc = [i[1] - pj[1] for i in points if i[0] == pj[0] and i[1] - pj[1] != 0]
#    fp = [i for i in points if i[0] == pj[0] or i[1] == pj[1]]
    x_d, y_d = 0, 0
    if len(xdc) > 0:
        max_xdc, min_xdc = max(xdc), min(xdc)
        x_d = min_xdc if max_xdc ** 2 <= min_xdc ** 2 else max_xdc
    if len(ydc) > 0:
        max_ydc, min_ydc = max(ydc), min(ydc)
        y_d = min_ydc if max_ydc ** 2 <= min_ydc ** 2 else max_ydc
    sx, sy = 0, 0
    if x_d ** 2 >= y_d ** 2:
        sx = x_d * 2
    else:
        sy = y_d * 2
    points[j - 1][0] += sx
    points[j - 1][1] += sy
    prev_p = j
print(abs((points[c1 - 1][0] - points[c2 - 1][0]) * (points[c1 - 1][1] - points[c2 - 1][1])))
