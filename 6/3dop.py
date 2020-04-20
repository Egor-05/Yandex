c = 0
d = 1
e = int(input())
for i in range(e):
    a = int(input())
    b = int(input())
    c = c * b + a * d
    d *= b
x = c
y = d
while y > 0:
    x, y = y, x % y
print(c // x, '/', d // x, sep='')