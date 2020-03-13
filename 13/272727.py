a = [0]
n = int(input())
for i in range(n):
    s = 0
    for j in range(len(a)):
        if a[j] == a[-1 - j]:
            s += 1
    a.append(s)
del a[-1]
for i in a:
    print(i)