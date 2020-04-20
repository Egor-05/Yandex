money = int(input())
chislo_skota = int(input())
for b in range(1, money // 20 + 1):
    for k in range((money - b * 20) // 10 + 1):
        t = chislo_skota - b - k
        if b * 20 + k * 10 + t * 5 == money:
            print(b, k, t)
