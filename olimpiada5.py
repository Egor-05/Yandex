a = int(input())
mushrooms = [int(i) for i in input().split()]
mm = min(mushrooms)
if mm == 0:
    print(0)
    exit()
d_f_r = [i for i in range(1, mm + 1) if mm % i == 0]
# d_f_r.sort()
for i in range(a):
    s = 0
    while s < len(d_f_r):
        if mushrooms[i] % d_f_r[s] != 0:
            del d_f_r[s]
        else:
            s += 1
print(max(d_f_r))
