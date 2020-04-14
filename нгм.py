import numpy as np


table = np.genfromtxt('ABBREV.csv', delimiter=';', dtype=None, names=True, encoding="utf8")
table.sort(order=['Energ_Kcal', 'Shrt_Desc'])
print(table[-1][1])
table.sort(order='Sugar_Tot_g')
a = [i[9] for i in table]
print(table[a.index(table[-1][9])][1])
table.sort(order='Protein_g')
a = [i[5] for i in table]
print(table[a.index(table[-1][5])][1])
table.sort(order='Vit_C_mg')
a = [i[20] for i in table]
print(table[-1][1])