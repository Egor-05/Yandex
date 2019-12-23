a = int(input())
l1 = []
l2 = []
itog = []
for _ in range(a):
    a1 = input()
    a2 = int(input())
    l2.append(a2)
    l2.append(a1)
    l1.append(l2)
    l2 = []
l1.sort(reverse=True)
if len(l1) % 2 != 0:
    l2 = l1[len(l1) // 2 + 1:]
    l1 = l1[:len(l1) // 2 + 1]
else:
    l2 = l1[len(l1) // 2:]
    l1 = l1[:len(l1) // 2]
for j in l1:
    del j[0]
l1.sort()
for j in l2:
    del j[0]
l2.sort()
l1 += l2
for i in l1:
    itog += i
print('\n'.join(itog))
