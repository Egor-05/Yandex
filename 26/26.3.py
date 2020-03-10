import sys
lst = []
for i in sys.stdin:
    if '\n' in i:
        i = i[:-1]
    i = i.split()
    lst.append([int(j) for j in i if j.isdigit()])
res = sum(lst[0])
if all([sum(x) == res for x in lst]) and all([sum(x) == res for x in list(zip(*lst))]):
    print('YES')
else:
    print('NO')