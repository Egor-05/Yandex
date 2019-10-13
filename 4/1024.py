a = int(input())
n = a
c = 0
while a > 1:
    a //= 2
    c += 1
if 2 ** c == n:
    print(c)
else:
    print('НЕТ')
