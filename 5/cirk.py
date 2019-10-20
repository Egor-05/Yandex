n, s, n1 = int(input()), 0, 1
while n1 != n:
    if (n1 * 2) < n:
        n1 *= 2
    elif (n1 * 2) >= n:
        n1 += 1
    s += 1
print(s)
