zaprosy = []
p = []
a = int(input())
for i in range(a):
    a1 = input()
    zaprosy.append(a1)
poiskel = int(input())
for b in range(poiskel):
    poisk = input()
    p.append(poisk)
for j in zaprosy:
    s = 0
    for e in p:
        if e in j:
            s += 1
    if s == len(p):
        print(j)