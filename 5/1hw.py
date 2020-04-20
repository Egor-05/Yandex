d = int(input())
m = int(input())
y = int(input())
if m <= 2:
    y -= 1
    m += 10
else:
    m -= 2
c = y // 100
y = y % 100
n = (d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)) % 7
print(n)
