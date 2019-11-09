angl = set()
nem = set()
franc = set()
a = int(input())
b = int(input())
c = int(input())
for i in range(a + b + c):
    a1 = input()
    if a1 in angl and a1 in franc:
        nem.add(a1)
    elif a1 in nem and a1 in franc:
        angl.add(a1)
    else:
        franc.add(a1)
diff1 = angl ^ nem
diff = diff1 ^ franc
if len(diff) == 0:
    print('NO')
else:
    print(len(diff))
