n1 = int(input())
n = n1
n1 -= 1
summ = 0
a4 = n // 60
summ += a4 * 440
n -= 60 * (n // 60)
a3 = n // 20
summ += a3 * 230
n -= 20 * (n // 20)
a2 = n // 10
summ += 125 * a2
n -= 10 * (n // 10)
a1 = n // 5
summ += 70 * a1
n -= 5 * (n // 5)
a0 = n // 1
summ += a0 * 15
n -= 1 * (n // 1)
if (n1 // 60 + 1) * 440 < summ:
    summ = (n1 // 60 + 1) * 440
    a4 = n1 // 60 + 1
    a3 = 0
    a2 = 0
    a1 = 0
    a0 = 0
if (n1 // 20 + 1) * 230 < summ:
    summ = (n1 // 20 + 1) * 230
    a4 = 0
    a3 = n1 // 20 + 1
    a2 = 0
    a1 = 0
    a0 = 0
if (n1 // 10 + 1) * 125 < summ:
    summ = (n1 // 10 + 1) * 125
    a4 = 0
    a3 = 0
    a2 = n1 // 10 + 1
    a1 = 0
    a0 = 0
if (n1 // 5 + 1) * 70 < summ:
    summ = (n1 // 5 + 1) * 70
    a4 = 0
    a3 = 0
    a2 = 0
    a1 = n1 // 5 + 1
    a0 = 0
if (n1 + 1) * 15 < summ:
    summ = (n1 + 1) * 15
    a4 = 0
    a3 = 0
    a2 = 0
    a1 = 0
    a0 = n1 + 1
print(a0, a1, a2, a3, a4, sep=' ')
