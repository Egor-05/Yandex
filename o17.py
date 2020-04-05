from fnmatch import fnmatch as fm


file = input()
mask = input()
delta = len(file) - len(mask) + 1
res = -1
for i in range(delta + 1):
    if fm(file, '?' * i + mask) or fm(file, mask + '?' * i):
        res = i if i < res or res == -1 else res
for s in range(1, delta + 1):
    e = delta - s
    if fm(file, '?' * s + mask + '?' * e):
        print(delta + 1)
        res = delta + 1 if delta + 1 < res or res == -1 else res
    for s1 in range(1, s + 1):
        e1 = delta - s1
        if fm(file, '?' * s1 + mask + '?' * e1) or fm(file, '?' * e1 + mask + '?' * s1):
            res = s if s < res or res == -1 else res
if res == -1:
    print('NO')
else:
    print(res)
