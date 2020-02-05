def check_pin(num):
    n1, n2, n3 = [int(i) for i in num.split('-')]
    s1 = 0
    for i in range(1, n1 + 1):
        if n1 % i == 0:
            s1 += 1
    n2r = str(n2)[::-1]
    while n3 > 1:
        n3 /= 2
    if int(s1) == 2 and int(n2r) == n2 and n3 == 1:
        return 'Корректен'
    else:
        return 'Некорректен'
