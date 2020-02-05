from math import sqrt
import datetime


def all_div(n):
    lst = []
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            if n % (i ** 2) == 0 or n % (n // i) ** 2 == 0:
                return False
            else:
                return True
    print(n, lst)
    return False


st, fn = [int(i) for i in input().split()]
res = []
for i in range(st, fn + 1):
    rr = all_div(i)
    if rr:
        res.append(i)
    print(i, rr, res)
if len(res):
    print(' '.join([str(i) for i in res]))
else:
    print('NO')
