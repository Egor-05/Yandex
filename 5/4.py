a = int(input())
while a > 0:
    a1 = int(input())
    if a1 > 3 or a1 < 1 or a1 > a:
        print(a)
    else:
        a -= a1
        print(a)
