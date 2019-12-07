n = int(input())
a = []
for i in range(n):
    s = input()
    sp = []
    while s != '*':
        sp.append('-'.join(s.split()))
        s = input()
    a.append('-'.join(sp))
print(', '.join(a[::-1]))
