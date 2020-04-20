a = int(input())
b = False
for i in range(a):
    a = input()
    if 'кот' in a or 'Кот' in a:
        b = True
        break
if b:
    print('МЯУ')
else:
    print('НЕТ')