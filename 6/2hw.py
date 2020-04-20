a = int(input()) - 1
b = 1
for i in range(a + 1):
    print(' ' * a + '*' * b)
    b += 2
    a -= 1
