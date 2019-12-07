a = input()
a = [int(i) for i in a.split()]
c = 0
d = 0
for j in a:
    if a.count(j) > d:
        c, d = j, a.count(j)
a.sort()
while len(a) != 1 and len(a) != 2:
    del a[0]
    del a[-1]
a.append(c)
for i in a:
    print(i, end=' ')
