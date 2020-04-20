a = int(input())
s = 0
for i in range(1, a + 1):
    n = int(input())
    s += n
    if n == s / i:
        print('0')
    elif n > s / i:
        print('>')
    else:
        print('<')
