a = float(input())
t = 0
while a >= 0:
    if a >= 1000:
        a = a * 0.95
    t += a
    a = float(input())
print(t)
