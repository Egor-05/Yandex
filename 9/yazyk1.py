angl = set()
nem = set()
a = int(input())
b = int(input())
for i in range(a + b):
    a1 = input()
    if a1 in angl:
        nem.add(a1)
    elif a1 not in angl:
        angl.add(a1)
diff = angl ^ nem
if len(diff) == 0:
    print('NO')
else:
    print(len(diff))
