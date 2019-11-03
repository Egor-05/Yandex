d = int(input())
m = int(input())
e = int(input())

c = int(e // 100)
y = ((e - c) % 100)

r = d + ((13 * m - 1) // 5) + y + (y // 4 + c // 4 - 2 * c + 777)
r %= 7
if m == 1 or m == 2:
    print(r + 2)
else:
    print(r)
