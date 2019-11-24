a = int(input())
sp = []
for i in range(a):
    cor = input()
    sp.append(cor)
a1 = int(input())
for j in range(a1):
    prov = input()
    for e in sp:
        if prov == e:
            print(e)
