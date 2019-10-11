a = input()
a1 = int(a) // 100
a2 = int(a) // 10 - a1 * 10
a3 = int(a) - a1 * 100 - a2 * 10
chast1 = str(a1 + a2)
chast2 = str(a2 + a3)
if chast1 < chast2:
    chast2, chast1 = chast1, chast2
print(chast2 + chast1)