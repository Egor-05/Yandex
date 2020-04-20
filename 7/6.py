stroka = 0
s = 0
kot = 0
prov = False
m = 0
while 1:
    a = int(input())
    if a == 0:
        break
    s += 1
    m += a
    if m == 10:
        prov = True
        kot += 1
        if kot == 1:
            stroka = s
print(stroka)

