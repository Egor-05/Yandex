a = int(input())
di = {}
li = []
for i in range(a):
    a1 = input().lower().split()
    for j in a1:
        for b in j:
            if b.isalpha() is False:
                j = j.replace(b, '')
        li.append(j)
el = set(li)
el = list(el)
el.sort()
for i in el:
    if i not in di:
        di[i] = li.count(i)
    else:
        di[i] += li.count(i)
l_k = list(di.keys())
l_k.sort()
d = sorted(di, key=di.get, reverse=True)
for i in range(len(d)):
    d[i] = d[i].capitalize()
print('\n'.join(d))
