n = int(input())
p = 0
itog = - 1
for i in range(n):
    b = int(input())
    h, r, m = b % 256, (b // 256) % 256, b // 256 ** 2
    t = ((m + r + p) * 37) % 256
    if t != h or h >= 100:
        itog = i
        break
    p = h
print(itog)
