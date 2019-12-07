a = int(input())
ev = []
med = []
moda = []
for i in range(a):
    c = 0
    s = 0
    b = []
    a1 = input().split()
    a1 = [int(j) for j in a1]
    a1.sort()
    ev += a1
    a2 = set(a1)
    med.append(a1[len(a1) // 2 + 1])
    for b in a2:
        if a1.count(b) > s:
            s, c = a1.count(b), b
    c = 0
    s = 0
    moda.append(c)
    moda.sort()
    print(med)
    print(moda)
    print(med[a // 2 + 1])
    for e in set(moda):
        if a1.count(e) > s:
            s, c = a1.count(e), e
    print(c)