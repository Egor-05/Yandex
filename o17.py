a = [input() for i in range(9)]
a1 = [a[i][j] for j in range(3) for i in range(3) if a[i][j].isdigit()]
a2 = [a[i][j] for j in range(3, 6) for i in range(3) if a[i][j].isdigit()]
a3 = [a[i][j] for j in range(6, 9) for i in range(3) if a[i][j].isdigit()]
a4 = [a[i][j] for j in range(3) for i in range(3, 6) if a[i][j].isdigit()]
a5 = [a[i][j] for j in range(3, 6) for i in range(3, 6) if a[i][j].isdigit()]
a6 = [a[i][j] for j in range(6, 9) for i in range(3, 6) if a[i][j].isdigit()]
a7 = [a[i][j] for j in range(3) for i in range(6, 9) if a[i][j].isdigit()]
a8 = [a[i][j] for j in range(3, 6) for i in range(6, 9) if a[i][j].isdigit()]
a9 = [a[i][j] for j in range(6, 9) for i in range(6, 9) if a[i][j].isdigit()]
b = [a1, a2, a3, a4, a5, a6, a7, a8, a9]
horiz = [[a[j][i] for j in range(9) if a[j][i].isdigit()] for i in range(9)]
vert = [[a[j][i] for j in range(9) if a[j][i].isdigit()] for i in range(9)]
prov = True
for i in b:
    if len(i) != len(set(i)):
        prov = False
        break
if prov:
    for i in vert:
        if len(i) != len(set(i)):
            prov = False
            break
if prov:
    for i in horiz:
        if len(i) != len(set(i)):
            prov = False
            break
print('YES' if prov else 'NO')
