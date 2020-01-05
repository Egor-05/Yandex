a = int(input())
koor = {}
sa = 0
for i in range(a):
    a1 = input().split()
    if len(a1[0]) == 1 and len(a1[1]) == 1:
        sa += 1
    if a1[0][:-1] not in koor:
        koor[a1[0][:-1]] = a1[1][:-1]
    else:
        koor[a1[0][:-1]] += ' ' + a1[1][:-1]
for i in koor:
    s = 0
    for j in koor[i]:
        if len(koor[i].split()) > s:
            s = len(koor[i].split())
    if s > sa:
        sa = s
print(sa)
