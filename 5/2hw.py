n = int(input())
s = 0
while n > 1:
    s += 1 + (n % 2)
    n = n // 2
print(s)
