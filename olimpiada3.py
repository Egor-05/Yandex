a = [int(i) for i in input().split()]
opos = [int(i) for i in input().split()]
row = []
for i in range(len(opos)):
    row += str(i + 1) * (a[1] - opos[i])
rbo = []
for i in range(len(opos)):
    rbo += str(i + 1) * (a[1] - opos[i])
endrow = ['.'] * a[0] * a[1]
s = 0
for i in range(a[0]):
    for j in range(len(endrow)):
        if (j + 1) % (i + 1) == 0 and opos[i] > 0:
            endrow[j] = str(i + 1) + 'o'
            opos[i] -= 1
for i in range(len(endrow)):
    if endrow[i] == '.':
        endrow[i] = rbo[0]
        del rbo[0]
#  for i in range(a[0]):
#      for j in range(opos[i]):
#          row.insert((j + 1) * (i + 1) - 1, i + 1)
print(endrow)
print(row)
zvezd = [0] * a[0]
for i in range(len(row) - a[-1], -1, a[-1] * -1):
    if row[i] == int(row[i]):
        zvezd[int(row[i][0]) - 1] += 1
print(' '.join([str(i) for i in zvezd]))
