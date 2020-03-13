from decimal import Decimal, getcontext
a = int(input())
getcontext().prec = 10000
a = Decimal(1) / Decimal(a)
a = str(a)
a = a[2:-1]
ex = False
for i in range(len(a)):
    for j in range(1, len(a)):
        res = [a[c:c + j] for c in range(i, len(a), j) if c + j <= len(a)]
        if len(set(res)) == 1 and len(res) > 1:
            print(res[0])
            ex = True
            break
    if ex:
        break
if ex is False:
    print(0)

