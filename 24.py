from sys import stdin
from collections import defaultdict


def way(p_now, arr, s):
    minn = 10 ** 10
    for i in from_to[p_now]:
        if i in arr:
            continue
        if i == end:
            return s
        if p_now == start:
            arr = []
            s = 0
        arr.append(i)
        w = way(i, arr, s)
        if w < minn:
            minn = w
            s += w
    return s


from_to = defaultdict(list)
len_way = {}
start = 0
end = 0
for i in stdin:
    i.strip('\n')
    a = i.split()
    if len(a) == 3:
        from_to[a[0]].append(a[1])
        from_to[a[1]].append(a[0])
        len_way[f'{a[0]}-{a[1]}'] = a[2]
        len_way[f'{a[1]}-{a[1]}'] = a[2]
    else:
        start, end = a
print(way(start, [], 0))