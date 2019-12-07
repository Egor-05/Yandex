a = int(input())
a = 1 / a
a = str(a)
a = a[2:]
a = [int(j) for j in a]
for i in range(len(a)):
    if a.count(a[i]) < 3:
        del a[i]
a1 = set(a)
print(a1)
