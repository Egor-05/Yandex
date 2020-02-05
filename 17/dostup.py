a = int(input())
dost = []
for i in range(a):
    adres = input().split('/')
    dost.append(adres)
a = int(input())
for i in range(a):
    f = input().split('/')
    s = 0
    for j in dost:
        if f[:len(j)] == j:
            s += 1
    if s > 0:
        print('YES')
    else:
        print('NO')
