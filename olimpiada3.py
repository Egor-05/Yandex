row = []
a = input().split()
a = [int(i) for i in a]
a[-1] = a[-1] - a[-1] * 2
for i in range(a[0]):
    a1 = ['n'] * a[1]
    row.append(a1)
opos = input().split()
opos = [int(i) for i in opos]
for i in range(len(row)):
    a1 = -1
    for j in range(opos[i]):
        a1 += opos[i]
        row[i].insert(a1, 'o')
print(row)
for i in range(len(row), 0, -1):
    fo
