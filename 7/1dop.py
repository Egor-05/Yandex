a = int(input())
prov = False
for i in range(a):
    a1 = input()
    if 'кот' in a1 or 'Кот' in a1:
        prov = True
    if 'пёс' in a1 or 'Пёс' in a1:
        prov = False
if prov:
    print('МЯУ')
else:
    print('НЕТ')
