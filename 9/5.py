angl = set()
nem = set()
france = set()
a = int(input())
b = int(input())
c = int(input())
for i in range(a + b + c):
    a1 = input()
    if a1 not in angl:
        angl.add(a1)
    elif a1 not in nem:
        nem.add(a1)
    elif a1 not in france:
        france.add(a1)
diff1 = angl & nem
diff2 = france & angl
diff3 = nem & france
diff4 = diff1 & diff2 & diff3
diff5 = diff3 ^ diff2 ^ diff1
diff = diff5 - diff4
if len(diff) == 0:
    print('NO')
else:
    print(len(diff))
