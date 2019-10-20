d = int(input())
m = int(input())
e = int(input())

c = e / 100
y = e - c * 100
w = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
r = w % 7
print(r)
