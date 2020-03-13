a = int(input())
dict_ = {}
for i in range(a):
    a1 = input().split()
    if a1[-1] not in dict_:
        dict_[a1[-1]] = {}
    dict_[a1[-1]][a1[1].rjust(2, '0') + a1[0]] = a1[0] + ' ' + a1[1]
a = int(input())
for j in range(a):
    pr = []
    a2 = input()
    if a2 in dict_:
        lk = list(dict_[a2].keys())
        lk.sort()
        for i in lk:
            pr.append(dict_[a2][i])
    print(' '.join(pr))
