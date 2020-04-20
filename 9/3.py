angl = set()
nem = set()
a = int(input())
b = int(input())
for i in range(a):
    a1 = input()
    angl.add(a1)
for j in range(b):
    b1 = input()
    nem.add(b1)
diff = angl ^ nem
if len(diff) == 0:
    print('NO')
else:
    print(len(diff))