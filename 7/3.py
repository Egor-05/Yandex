stroka = 0
s = 0
kot = 0
prov = False
while 1:
    a = input()
    if a == 'СТОП':
        break
    s += 1
    if 'кот' in a or 'Кот' in a:
        prov = True
        kot += 1
        if kot == 1:
            stroka = s
if prov is True:
    print(stroka)
else:
    print('-1')