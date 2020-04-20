a = input()
b = int(input())
c = len(a)
if b <= 0 or b > c:
    print('ОШИБКА')
else:
    print(a[b - 1])