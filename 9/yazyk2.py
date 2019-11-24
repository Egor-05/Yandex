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
diff1 = angl & nem & france
diff2 = (angl & nem) ^ (nem & france) ^ (france & angl)
diff = diff2 - diff1
if len(diff) == 0:
    print('NO')
else:
    print(len(diff))
