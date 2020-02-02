from math import sqrt


def chk_div(n):
    lst = set()
    lst.add(n)
    n1 = int(sqrt(n))
    for i in range(2, n1 + 1):
        if n % i == 0:
            if i * i in lst or sqrt(i) in lst:
                return False
            lst.add(i)
            n2 = n // i
            if n2 * n2 in lst or sqrt(n2) in lst:
                return False
            lst.add(n2)
    if len(lst) > 1:
        return True
    return False


st, fn = [int(i) for i in input().split()]
res = [str(i) for i in range(st, fn + 1) if chk_div(i)]
if len(res):
    print(' '.join(res))
else:
    print('NO')
