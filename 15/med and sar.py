a = input()
a = [float(i) for i in a.split()]
print(sum(a) / len(a), end=' ')
a.sort()
while len(a) != 1 and len(a) != 2:
    del a[0]
    del a[-1]
print(sum(a) / len(a))
