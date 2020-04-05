from sys import stdin


a = [i for i in input().split('\t')][1:]
b = []
names = []
for i in stdin:
    a1 = [i.strip() for i in i.split('\t')]
    names.append(a1[0])
    b.append(a1[1:])
c = [[int(j) for j in i[0]] for i in zip(b)]
mx = c.index(min(c, key=lambda x: sum(x)))
c = [str(i) for i in c[mx]]
print(names[mx])
for i in range(len(c)):
    print(f'{a[i]}\t{c[i]}')
