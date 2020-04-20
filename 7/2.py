a = int(input())
b = False
for i in range(a):
    a1 = input()
    if 'кот' in a1 or 'Кот' in a1:
        b = True
if b is True:
    print('МЯУ')
else:
    print('НЕТ')