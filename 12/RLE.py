a = input()
a = [int(i) for i in a]
a1 = set(b for b in a)
k = 0
for j in range(len(a)):
    for e in a1:
        if j == e:
            k += 1
    if a[j] <= len(a):
        if a[j] != a[j + 1]:
            print(k, a[j])
            k = 0
    else:
        if a[j] != a[j - 1]:
            print(k, a[j - 1])
            k = 0
