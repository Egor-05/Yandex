a = [int(i) for i in input().split()]
opos = [int(i) for i in input().split()]
row = []
for i in range(len(opos)):
    row += str(i + 1) * (a[1] - opos[i])
for i in range(a[0]):
    for j in range(opos[i]):
        row.insert((j + 1) * (i + 1) - 1, i + 1)
zvezd = [0] * a[0]
for i in range(len(row) - a[-1], -1, a[-1] * -1):
    if row[i] == int(row[i]):
        zvezd[row[i] - 1] += 1
print(' '.join([str(i) for i in zvezd]))
