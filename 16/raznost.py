a = int(input())
a1 = []
for _ in range(a):
    a1.append(int(input()))
a2 = set()
for i in a1:
    for j in a1:
        a2.add(i - j)
a3 = list(a2)
a3.sort()
print('\n'.join([str(e) for e in a3]))
