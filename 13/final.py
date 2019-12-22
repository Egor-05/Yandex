a = int(input())
l1 = []
for _ in range(a):
    l2 = []
    a1 = input()
    a2 = int(input())
    l2.append(a2)
    l2.append(a1)
    l1.append(l2)
l1.sort(reverse=True)
l2 = l1[len(l1) // 2:]
if len(l1) % 2 != 0:
    l1 = l1[:len(l1) // 2 + 1]
else:
    l1 = l1[:len(l1) // 2]
l2.sort()
l1 += l2
for j in l1:
    del j[0]
for i in l1:
    i = str(i)
    print(i[2:-2])
