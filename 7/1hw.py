stroka = 0
s = 0
kot = 0
prov = False
kote = 0
while 1:
    a = input()
    if a == 'СТОП':
        break
    s += 1
    if 'кот' in a or 'Кот' in a:
        kote += 1
        if kote == 1:
            stroka = s
        kot += 1
        prov = True
if prov:
    print(kot, stroka)
else:
    print(kot, -1)