for i in range(1, 10000):
    s1 = 0
    s2 = 0
    for b in range(1, i):
        if i % b == 0:
            s1 += b
    if i >= s1:
        continue
    for a in range(1, s1):
        if s1 % a == 0:
            s2 += a
    if i == s2:
        print(i, s1)
