a = int(input())
dict_ = {}
for i in range(a):
    a1 = input().split()
    if a1[-1] in dict_:
        dict_[a1[-1]].append({a1[1]: a1[0]})
    else:
        dict_[a1[-1]] = [{a1[1]: a1[0]}]
a = int(input())
for j in range(a):
    a2 = input()
    if a2 in dict_:
        dict_[a2].sort()
        b = []
        for i in dict_[a2]:
            i = i.split()
            i.reverse()
            b.append(' '.join(i))
        print(' '.join(b))
    else:
        print()
