from sys import stdin
from collections import defaultdict


def way(p_now, arr):
    arr.append(p_now)
    for i in from_to[p_now]:
        if i == end:
            global ways
            arr1 = arr + [i]
            ways[sum([from_to[arr1[j]][arr1[j + 1]] for j in range(len(arr1) - 1)])] = ', '.join(arr1)
        elif i in arr:
            continue
        else:
            way(i, arr.copy())


from_to = defaultdict(dict)
ways = {}
start = 0
end = 0
for i in stdin:
    i.strip('\n')
    a = i.split()
    if len(a) == 3:
        from_to[a[0]][a[1]] = int(a[2])
        from_to[a[1]][a[0]] = int(a[2])
    else:
        start, end = a
way(start, [])
print(ways[min(list(ways.keys()))])