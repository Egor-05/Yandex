a = int(input())
b = int(input())
t1 = []
for i in range(a):
    t = []
    for j in range(b):
        a = input()
        t.append(a)
    t1.append(t)
print('\t'.join(t1[0]))
if len(t1) > 1:
    for e in range(1, len(t1) - 1):
        t1[e].sort()
        print('\t'.join(t1[e]))
    print('\t'.join(t1[-1]))
