a = int(input())
b = int(input())

c = 0
d = 0

while a == 0 or b == 0:
    c = int(input())
    d = int(input())

    if c == 1:
        if a - d >= 0:
            a -= d
    else:
        if b - d >= 0:
            b -= d

    print(a, b)