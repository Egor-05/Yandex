med = []
mod = []
al = []
for j in range(int(input())):
    s = list(map(int, input().split()))
    s.sort()
    b = s[len(s) // 2]
    a = 0
    c = 0
    for i in s:
        if s.count(i) > a:
            a = s.count(i)
            c = i
    med.append(b)
    mod.append(c)
    for i in s:
        al.append(i)
al.sort()
me = [str(i) for i in med]
mo = [str(i) for i in mod]
print(' '.join(me))
print(' '.join(mo))
med.sort()
mod.sort()
print(med[len(med) // 2])
print(mod[len(mod) // 2])
print(al[len(al) // 2])
a = 0
c = 1234
for i in al:
    if al.count(i) > a:
        a = al.count(i)
        c = i
print(c)
